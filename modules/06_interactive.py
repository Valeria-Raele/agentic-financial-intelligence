# ========= ORIGINAL NOTEBOOK CELL 66 =========
# ============================================================
# BOX 50 — REAL INPUT FOR THE AGENTIC SYSTEM
# ============================================================

if "conversation_history" not in globals():
    conversation_history = []

# Maximum width of printed lines
PRINT_WIDTH = 90


import re
import textwrap

# Presentation-only filter: keep the generated answer and history unchanged.
_INTERNAL_EVIDENCE_ID = r"STEP_\d+::[A-Za-z_][\w]*(?:::\d+(?:-\d+)?)?"
_INTERNAL_EVIDENCE_GROUP = re.compile(
    r"\(\s*" + _INTERNAL_EVIDENCE_ID +
    r"(?:\s*[,;]\s*" + _INTERNAL_EVIDENCE_ID + r")*\s*\)"
)
_INTERNAL_EVIDENCE_STANDALONE = re.compile(_INTERNAL_EVIDENCE_ID)


def clean_display_answer(text):
    """Remove only internal evidence references from a display copy."""
    text = str(text)
    text = _INTERNAL_EVIDENCE_GROUP.sub("", text)
    text = _INTERNAL_EVIDENCE_STANDALONE.sub("", text)
    text = re.sub(r"\(\s*[,;\s]*\)", "", text)
    text = re.sub(r"[ \t]+([.,;:])", r"\1", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text


def print_wrapped_text(text, width=PRINT_WIDTH):
    """
    Prints the text across multiple lines while keeping
    the output readable without modifying the content.
    """
    text = str(text).strip()

    paragraphs = text.splitlines()

    for paragraph in paragraphs:

        if not paragraph.strip():
            print()
            continue

        print(
            textwrap.fill(
                paragraph,
                width=width,
                break_long_words=False,
                break_on_hyphens=False
            )
        )


print("\nInteractive session ready. Enter a financial question.")
print("Type 'exit' to end the session. ('quit' and 'end' also work.)")

while True:
    try:
        question = input("\nQUESTION > ")
    except (EOFError, KeyboardInterrupt):
        print("\nSession ended.")
        break

    if question.strip().lower() in {"exit", "quit", "end"}:
        print("\nSession ended.")
        break

    if not question.strip():
        continue

    result = ask_agentic_system(
        question,
        base_state=final_state,
        update_global_state=True,
        register_history=True
    )

    answer = result["final_answer"]

    conversation_history.append(
        {
            "question": question,
            "answer": answer
        }
    )

    print("\n" + "=" * 100)
    print("\nQUESTION >\n")
    print_wrapped_text(question)
    print("\nANSWER >\n")
    print_wrapped_text(clean_display_answer(answer))
    print("\n" + "=" * 100)
