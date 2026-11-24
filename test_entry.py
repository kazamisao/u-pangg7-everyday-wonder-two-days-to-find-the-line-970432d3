"""Checks for the Everyday Wonder entry.

Run with: python3 test_entry.py
Verifies the written sentence is a single line of 1-200 characters and
is byte-identical across two runs.
"""

import os
import tempfile
from pathlib import Path

import main


def run_once() -> str:
    with tempfile.TemporaryDirectory() as tmp:
        os.environ["MAKEFUN_OUTPUT_DIR"] = tmp
        main.main()
        return (Path(tmp) / "entry.txt").read_text(encoding="utf-8")


def test_entry() -> None:
    text = run_once()
    assert text == run_once(), "entry must be deterministic"
    assert 1 <= len(text) <= 200, f"length {len(text)} outside 1-200"
    assert text.strip(), "entry must not be blank"
    assert "\n" not in text, "entry must be a single line"
    print(f"ok: {len(text)} chars, single line, deterministic")


if __name__ == "__main__":
    test_entry()
