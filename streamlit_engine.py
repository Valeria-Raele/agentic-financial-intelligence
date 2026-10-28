"""Load and invoke the existing agentic financial engine from Streamlit.

The five computational stages share one namespace by design. The sixth module
is a Colab command-line interface and is not executed by Streamlit.
"""

import threading
from pathlib import Path

BASE = Path(__file__).resolve().parent
STAGES = ("01_setup", "02_market_pipeline", "03_quantitative", "04_documents", "05_reasoning")
LOCK = threading.RLock()


def initialize_engine(secrets=None):
    """Initialize the unchanged computational modules in dependency order.

    Module 01 resolves Streamlit secrets itself. No Colab module emulation or
    pandas monkeypatching is necessary in this adapter.
    """
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
    """Execute a question while protecting the engine's shared globals."""
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
            raise RuntimeError("The engine returned no valid question state.")

        errors = question_state.get("tool_execution_errors")
        trace = question_state.get("execution_trace")
        failed = isinstance(errors, (list, tuple, dict)) and bool(errors)
        if isinstance(trace, (list, tuple)):
            failed = failed or any(
                isinstance(step, dict)
                and str(step.get("status", "")).upper() == "FAILED"
                and "financial_metrics" in str(step.get("selected_tool", step.get("tool", ""))).lower()
                for step in trace
            )
        if failed and ("financial_metrics" in str(errors).lower() or "financial_metrics" in str(trace).lower()):
            raise RuntimeError(
                "A required financial_metrics tool execution failed; inspect the tool execution state."
            )
        return str(answer), question_state
