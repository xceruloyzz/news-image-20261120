"""Copy the finished front page to the grading output folder.

The entry image lives in this repository as entry.png. This program
does nothing but hand that file to the grader, in the place the
grader looks for it:

1. the directory named by MAKEFUN_OUTPUT_DIR, when that variable is set;
2. /output, when that directory already exists;
3. ./out, as a local fallback.

It refuses to run if entry.png is missing, so a broken build fails
loudly instead of submitting an empty output. Standard library only,
no network, no clock, and the copy is byte for byte.
"""

import os
import shutil
import sys
from pathlib import Path


def choose_destination() -> Path:
    """Pick the output folder using the priority listed above."""
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if wanted:
        return Path(wanted)
    if Path("/output").is_dir():
        return Path("/output")
    return Path("out")


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        print("entry.png is missing from the repository root", file=sys.stderr)
        return 1
    destination_dir = choose_destination()
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination = destination_dir / "entry.png"
    shutil.copyfile(source, destination)
    print(f"copied entry.png to {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
