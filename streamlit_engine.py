"""Streamlit adapter for the existing six-module agentic engine."""
import os
import sys
import types
import threading
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
        # The engine returns the updated state as the result itself.
        return str(answer), result
