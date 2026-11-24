"""Everyday Wonder (make.fun).

Writes one single sentence to $MAKEFUN_OUTPUT_DIR/entry.txt: a small
moment of wonder in everyday life. Chewing alone in a quiet kitchen,
the narrator's jaw cracks, and for a second the body becomes a cave
listening to its own rocks settle. Deterministic, stdlib only, no
network.
"""

import os
from pathlib import Path

SENTENCE = (
    "Chewing alone in a quiet kitchen, my jaw cracked \u2014 and "
    "for one small second I was a cave, listening to its own "
    "rocks settle in the dark."
)


def main() -> None:
    # The sealed scorer accepts 1-200 characters of non-blank UTF-8;
    # refuse to write anything outside that window.
    if not 1 <= len(SENTENCE) <= 200 or not SENTENCE.strip():
        raise ValueError(f"sentence is {len(SENTENCE)} characters, must be 1-200")
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(SENTENCE, encoding="utf-8")


if __name__ == "__main__":
    main()
