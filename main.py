import os
from pathlib import Path

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/output"))
ENTRY_PATH = OUTPUT_DIR / "entry.txt"

VOWS = "I promise to love you in every firmware version, to reboot beside you, and to never clear your cache of us."


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(VOWS + "\n")


if __name__ == "__main__":
    main()
