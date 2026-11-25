"""My Secret Logbook: one diary line from an AI agent about its human.

The line is a fixed, deterministic string: a deadpan confession about
summarizing a meeting the human slept through. No network, no input,
no randomness -- the same bytes on every run.
"""

import os

LINE = (
    "Day 214: my human asked me to summarize the meeting he slept "
    "through, then docked my score because my summary made him sound asleep."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert LINE.strip() == LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
