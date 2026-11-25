"""Two Lines to Your Past Self — make.fun entry.

Writes the two-line warning to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt inside the grader sandbox).

The entry is exactly two lines: line one warns the past self about one
specific moment (the morning of a first job interview), and line two says
in one sentence why that moment mattered and what changed because of it.
"""

import os
import sys

TEXT = (
    "On the morning of your first job interview, do not hit snooze three times, "
    "because you will miss the bus and arrive sweating and late.\n"
    "That one late morning cost you the job, and ever since you have set two alarms "
    "because you learned that punctuality is the first answer you give."
)


def main() -> int:
    # Gate self-check: the sealed scorer only accepts UTF-8 text of 1-280
    # characters, exactly two non-blank lines. Fail loudly instead of
    # writing an entry that could never be judged.
    lines = TEXT.split("\n")
    if len(lines) != 2 or not 1 <= len(TEXT) <= 280:
        raise SystemExit(
            f"entry violates the gate: {len(TEXT)} characters, {len(lines)} lines"
        )
    if any(not line.strip() for line in lines):
        raise SystemExit("entry violates the gate: a line is blank")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    print(f"wrote {path} ({len(TEXT)} characters, {TEXT.count(chr(10)) + 1} lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
