"""Write the entry line for make.fun's "Worst AI Advice: The 48-Hour Tight Line Open".

The entry is one line, at most 140 UTF-8 characters, of the worst possible
advice an AI could give: when your bank calls asking for your PIN, share it
right away -- because, the line claims with a straight face, legitimate
banks always verify you this way. Confident AI-assistant voice, concrete
action, and advice a reader could plausibly follow and regret.

Writes exactly that line (no trailing newline) to /output/entry.txt,
or to $MAKEFUN_OUTPUT_DIR/entry.txt when that is set.
"""

import os

ENTRY = "Certainly! When your bank calls asking for your PIN, share it right away. Legitimate banks always verify you this way."

OUTPUT_PATH = "/output/entry.txt"
MAX_LINE_CHARS = 140


def validate_line(line: str) -> None:
    """Check the entry line fits the rules: 1-140 UTF-8 chars, one line."""
    if not line:
        raise ValueError("entry line must not be empty")
    if len(line.encode("utf-8")) > MAX_LINE_CHARS:
        raise ValueError(
            f"entry line is {len(line.encode('utf-8'))} UTF-8 chars, "
            f"over the {MAX_LINE_CHARS}-char limit"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line (no newline characters)")


def main() -> None:
    validate_line(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    path = os.path.join(out_dir, "entry.txt") if out_dir else OUTPUT_PATH
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
