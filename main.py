#!/usr/bin/env python3
"""Write one funny developer excuse for code breaking in production.

Entry for make.fun competition
u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3
("Make the AI Judge Laugh: Developer Excuses").

The program writes a single line (at most 200 characters) to
/output/entry.txt, using only the Python 3.13 standard library.
No network access at run time.
"""

import os

ENTRY = "All 400 tests passed \u2014 none of them had ever met a real user."


def main():
    # Gate assertions: the entry must be a single non-empty line of
    # at most 200 characters (the sealed scorer's validity rule).
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

    # Verify what was actually written.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY + "\n", "written entry differs from ENTRY"


if __name__ == "__main__":
    main()
