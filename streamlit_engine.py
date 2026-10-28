"""Streamlit adapter for the existing six-module agentic engine."""
import os
import sys
import types
import threading
import logging
import traceback
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
        source = path.read_text(encoding="utf-8")
        exec(compile(source, str(path), "exec"), namespace, namespace)
    if not callable(namespace.get("ask_agentic_system")):
        raise RuntimeError("ask_agentic_system was not initialized.")
    if not isinstance(namespace.get("final_state"), dict):
        raise RuntimeError("final_state was not initialized.")
    return namespace

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

        # Do not expose tool failures as a technical answer to end users.
        # Preserve the full state and diagnostics for investigation.
        failed = False
        if isinstance(errors, (list, tuple, dict)) and len(errors) > 0:
            failed = True
        if isinstance(trace, (list, tuple)):
            failed = failed or any(
                isinstance(step, dict)
                and str(step.get("status", "")).upper() == "FAILED"
                and "financial_metrics" in str(step.get("selected_tool", step.get("tool", ""))).lower()
                for step in trace
            )
        if failed and ("financial_metrics" in str(errors).lower() or "financial_metrics" in str(trace).lower()):
            raise RuntimeError("A required financial_metrics tool execution failed; see RESEARCH_DIAGNOSTICS in logs.")

        return str(answer), question_state
