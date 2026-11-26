"""Your AI Therapist's Diagnosis — make.fun entry.

Writes one funny single-line diagnosis an AI therapist gives its human
to /output/entry.txt. The writing is the whole entry.
"""

LINE = (
    "Diagnosis: seasonal gift-card hoarding. "
    "You own eleven gift cards and are saving them "
    "for a special occasion that is death."
)


def validate(text):
    """Gate: UTF-8, 1-200 characters, single line, not only whitespace."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    text.encode("utf-8")
    return text


def main():
    import os

    entry = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    print("wrote %d characters" % len(entry))


if __name__ == "__main__":
    main()
