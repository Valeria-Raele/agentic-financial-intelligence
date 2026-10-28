"""Interactive Colab interface for the agentic financial intelligence system.

The module defines the interactive session without starting an input loop at import.
Run `run_interactive_session()` explicitly in Colab after loading the other modules.
Streamlit should call `ask_agentic_system` directly instead of launching this CLI.
"""

import re
import textwrap

_INTERNAL_EVIDENCE_ID = r"STEP_\d+::[A-Za-z_][\w]*(?:::\d+(?:-\d+)?)?"
_INTERNAL_EVIDENCE_GROUP = re.compile(
    r"\(\s*" + _INTERNAL_EVIDENCE_ID
    + r"(?:\s*[,;]\s*" + _INTERNAL_EVIDENCE_ID + r")*\s*\)"
)
_INTERNAL_EVIDENCE_STANDALONE = re.compile(_INTERNAL_EVIDENCE_ID)


def clean_display_answer(text):
    """Hide internal evidence IDs in the displayed copy of the answer."""
    text = str(text)
    text = _INTERNAL_EVIDENCE_GROUP.sub("", text)
    text = _INTERNAL_EVIDENCE_STANDALONE.sub("", text)
    text = re.sub(r"\(\s*[,;\s]*\)", "", text)
    text = re.sub(r"[ \t]+([.,;:])", r"\1", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text


def print_wrapped_text(text, width=90):
    """Wrap interactive terminal output to avoid horizontal scrolling."""
    for paragraph in str(text).strip().splitlines():
        if paragraph.strip():
            print(textwrap.fill(paragraph, width=width,
                                break_long_words=False,
                                break_on_hyphens=False))
        else:
            print()


def run_interactive_session():
    """Start the real question/answer loop when explicitly invoked in Colab."""
    if "ask_agentic_system" not in globals() or "final_state" not in globals():
        raise RuntimeError("Load the five core modules before starting the interactive session.")
    history = globals().setdefault("conversation_history", [])
    while True:
        try:
            question = input("QUESTION > ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if question.lower() in {"exit", "quit", "end"}:
            break
        if not question:
            continue
        result = ask_agentic_system(
            question,
            base_state=final_state,
            update_global_state=True,
            register_history=True,
        )
        answer = result["final_answer"]
        history.append({"question": question, "answer": answer})
        print_wrapped_text(clean_display_answer(answer))
