"""
RA-MARS Citation Coverage Checker

Checks citation placeholders in manuscript markdown against numbered references.
"""

import re
from pathlib import Path


MANUSCRIPT = Path("manuscript/RA-MARS-journal-draft-with-figures.md")


def expand_citation_token(token):
    token = token.strip()

    # Handle ranges like 30–33 or 30-33
    if "–" in token:
        start, end = token.split("–")
        return list(range(int(start), int(end) + 1))

    if "-" in token:
        start, end = token.split("-")
        return list(range(int(start), int(end) + 1))

    return [int(token)]


def main():
    text = MANUSCRIPT.read_text()

    # Citation groups like [1,5,30,39–41]
    citation_groups = re.findall(r"\[([0-9,\-\–\s]+)\]", text)

    used = set()
    for group in citation_groups:
        for token in group.split(","):
            token = token.strip()
            if token:
                used.update(expand_citation_token(token))

    # Reference list entries like [1] Author...
    reference_numbers = set(
        int(num) for num in re.findall(r"^\[(\d+)\]\s", text, flags=re.MULTILINE)
    )

    missing_refs = sorted(used - reference_numbers)
    uncited_refs = sorted(reference_numbers - used)

    print(f"Used citation numbers: {sorted(used)}")
    print(f"Reference list numbers: {sorted(reference_numbers)}")
    print(f"Missing references for used citations: {missing_refs}")
    print(f"References not cited in manuscript: {uncited_refs}")

    if missing_refs:
        raise SystemExit("ERROR: Some citations do not have matching references.")

    print("Citation coverage check completed successfully.")


if __name__ == "__main__":
    main()
