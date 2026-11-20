#!/usr/bin/env python3
"""Write the committed front page to the grading output directory.

The picture lives next to this file as entry.png. This program only moves
bytes around: it reads entry.png and writes an identical copy to wherever
the grader expects it, preferring $MAKEFUN_OUTPUT_DIR, then /output when
that directory exists, and finally ./out.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
IMAGE = HERE / "entry.png"


def pick_destination() -> Path:
    """Return the full path the copy should be written to."""
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if wanted:
        return Path(wanted) / "entry.png"
    if Path("/output").is_dir():
        return Path("/output") / "entry.png"
    return Path("out") / "entry.png"


def main() -> None:
    if not IMAGE.is_file():
        raise SystemExit(f"missing {IMAGE}: render it first with tools/generate_frontpage.py")
    dest = pick_destination()
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(IMAGE, dest)
    print(f"entry.png ({dest.stat().st_size} bytes) -> {dest}")


if __name__ == "__main__":
    main()
