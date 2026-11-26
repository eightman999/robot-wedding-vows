import os
from pathlib import Path

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/output"))
ENTRY_PATH = OUTPUT_DIR / "entry.txt"

VOWS = "I vow to share my charging port, defend your uptime, and love you even when your update restarts you mid-sentence."


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(VOWS + "\n")


if __name__ == "__main__":
    main()
