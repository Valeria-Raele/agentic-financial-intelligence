"""Gradio adapter for the existing six-module agentic engine."""
import os
import sys
import types
import threading
import logging
import traceback
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
STAGES = ("01_setup", "02_market_pipeline", "03_quantitative", "04_documents", "05_reasoning")
LOCK = threading.RLock()

def _install_colab_secrets_adapter(secrets):
    """Supply the existing modules' google.colab.userdata.get interface."""
    try:
        from google.colab import userdata
        return
    except ImportError:
        pass
    google = sys.modules.get("google")
    if google is None:
        google = types.ModuleType("google")
        google.__path__ = []
        sys.modules["google"] = google
    colab = types.ModuleType("google.colab")
    class UserData:
        @staticmethod
        def get(name):
            value = secrets.get(name, os.environ.get(name))
            if not value:
                raise RuntimeError(f"Missing required secret: {name}")
            return str(value)
    colab.userdata = UserData()
    google.colab = colab
    sys.modules["google.colab"] = colab

def initialize_engine(secrets):
    _install_colab_secrets_adapter(secrets)
    namespace = {"__name__": "__main__", "__file__": str(BASE / "run.py")}
    for stage in STAGES:
        path = BASE / "modules" / f"{stage}.py"
        if not path.exists():
            path = BASE / f"{stage}.py"
        if not path.exists():
            raise FileNotFoundError(f"Missing agentic module: {stage}.py. Place it in modules/ or alongside app.py")
        source = path.read_text(encoding="utf-8")
        exec(compile(source, str(path), "exec"), namespace, namespace)
    if not callable(namespace.get("ask_agentic_system")):
        raise RuntimeError("ask_agentic_system was not initialized.")
    if not isinstance(namespace.get("final_state"), dict):
        raise RuntimeError("final_state was not initialized.")
    return namespace

def clean_display_answer(text):
    """Remove internal evidence references from display text only."""
    text = str(text)
    text = re.sub(r"\(\s*STEP_\d+::[A-Za-z_]\w*(?:::\d+(?:-\d+)?)?(?:\s*[,;]\s*(?:(?:STEP_\d+::[A-Za-z_]\w*::)?|::)\d+(?:-\d+)?)*\s*\)", "", text)
    text = re.sub(r"STEP_\d+::[A-Za-z_]\w*(?:::\d+(?:-\d+)?)?", "", text)
    text = re.sub(r"\(\s*[,;\s:]*\)", "", text)
    text = re.sub(r"[ \t]+([.,;:])", r"\1", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text

def ask(engine, question, state):
    # The original engine uses module globals. Serialize calls to avoid concurrent access.
    with LOCK:
        result = engine["ask_agentic_system"](
            question,
            base_state=state,
            update_global_state=False,
            register_history=True,
        )
        if not isinstance(result, dict):
            raise RuntimeError("Unexpected engine response.")
        answer = result.get("final_answer")
        if not answer:
            raise RuntimeError("The engine returned no final_answer.")
        question_state = result.get("question_final_state")
        if not isinstance(question_state, dict):
            logging.error("RESEARCH_DIAGNOSTICS: missing question_final_state; keys=%s", list(result))
            raise RuntimeError("The engine returned no valid question state.")

        errors = question_state.get("tool_execution_errors")
        trace = question_state.get("execution_trace")
        logging.warning("RESEARCH_DIAGNOSTICS: question=%r", question)
        logging.warning("RESEARCH_DIAGNOSTICS: tool_execution_errors=%r", errors)
        logging.warning("RESEARCH_DIAGNOSTICS: execution_trace=%r", trace)
        logging.warning("RESEARCH_DIAGNOSTICS: execution_status=%r", question_state.get("execution_status"))

        # Block only confirmed financial_metrics execution failures.
        # The presence of financial_metrics in a successful trace
        # is not, by itself, evidence of failure.

        def is_financial_metrics_failure(item):
            if not isinstance(item, dict):
                return False

            tool_name = str(
                item.get("selected_tool")
                or item.get("tool")
                or item.get("tool_name")
                or ""
            ).lower()

            status = str(item.get("status", "")).upper()

            return (
                "financial_metrics" in tool_name
                and status in {"FAILED", "ERROR"}
            )

        trace_failed = (
            isinstance(trace, (list, tuple))
            and any(is_financial_metrics_failure(step) for step in trace)
        )

        if trace_failed:
            raise RuntimeError(
                "A required financial_metrics tool execution failed; "
                "see RESEARCH_DIAGNOSTICS in logs."
            )

        return clean_display_answer(answer), question_state
