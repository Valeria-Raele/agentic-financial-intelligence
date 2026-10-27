"""Sequential Colab-compatible runner preserving the original notebook global state."""
import argparse
from pathlib import Path

BASE = Path(__file__).resolve().parent
STAGES = [
    ("01_setup", "Configuration and connections"),
    ("02_market_pipeline", "Market data and validation"),
    ("03_quantitative", "Quantitative analysis"),
    ("04_documents", "Financial documents"),
    ("05_reasoning", "Agentic reasoning and querying"),
    ("06_interactive", "Interactive question input"),
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--through", choices=[name for name, _ in STAGES], default="05_reasoning")
    parser.add_argument("--start", choices=[name for name, _ in STAGES], default="01_setup")
    parser.add_argument("--check", action="store_true", help="Syntax check only; no API calls")
    args = parser.parse_args()
    names = [name for name, _ in STAGES]
    if names.index(args.start) > names.index(args.through):
        parser.error("--start must precede or equal --through")
    namespace = {"__name__": "__main__", "__file__": str(BASE / "run.py")}
    for name, label in STAGES:
        source_path = BASE / "modules" / (name + ".py")
        source = source_path.read_text(encoding="utf-8")
        compiled = compile(source, str(source_path), "exec")
        if args.check:
            print(f"PASS: {name} ({label})")
            continue
        if names.index(name) < names.index(args.start) or names.index(name) > names.index(args.through):
            continue
        print(f"\n{'=' * 65}\nRUNNING: {name} — {label}\n{'=' * 65}", flush=True)
        exec(compiled, namespace, namespace)
        print(f"COMPLETED: {name}", flush=True)
    if args.check:
        print("All modules compiled. This is NOT an end-to-end execution test.")
    else:
        # Expose the shared execution state to the calling Colab notebook (%run).
        globals().update({
            key: value for key, value in namespace.items()
            if key not in {"__name__", "__file__", "__builtins__"}
        })


if __name__ == "__main__":
    main()
