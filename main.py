"""Weirdest Job Title entry.

Writes exactly one job title — a real-sounding role with one
gloriously specific twist — to /output/entry.txt. Deterministic:
no input, no network, no randomness, same bytes every run.
"""

from pathlib import Path

ENTRY = "Senior Apologiser for Billionaires' Tweets"
OUTPUT = Path("/output/entry.txt")


def validate(text: str) -> str:
    if not (1 <= len(text) <= 60):
        raise ValueError(f"entry must be 1-60 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be blank")
    return text


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(validate(ENTRY), encoding="utf-8")


if __name__ == "__main__":
    main()
