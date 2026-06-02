"""
Final v3 citation coverage checker.
Checks whether numbered citations in final v3 manuscript match reference list entries.
"""

import re
from pathlib import Path

MANUSCRIPT = Path("manuscript/RA-MARS-journal-draft-final-v3.md")


def expand_token(token):
    token = token.strip()
    if not token:
        return []

    if "–" in token:
        start, end = token.split("–")
        return list(range(int(start), int(end) + 1))

    if "-" in token:
        start, end = token.split("-")
        return list(range(int(start), int(end) + 1))

    return [int(token)]


def main():
    if not MANUSCRIPT.exists():
        raise FileNotFoundError(f"Final v3 manuscript not found: {MANUSCRIPT}")

    text = MANUSCRIPT.read_text()

    citation_groups = re.findall(r"\[([0-9,\-\–\s]+)\]", text)

    used = set()
    for group in citation_groups:
        for token in group.split(","):
            token = token.strip()
            if token:
                used.update(expand_token(token))

    refs = set(
        int(num) for num in re.findall(r"^\[(\d+)\]\s", text, flags=re.MULTILINE)
    )

    missing_refs = sorted(used - refs)
    uncited_refs = sorted(refs - used)

    print("Used citation numbers:", sorted(used))
    print("Reference list numbers:", sorted(refs))
    print("Missing references for used citations:", missing_refs)
    print("References not cited in manuscript:", uncited_refs)

    if missing_refs:
        raise SystemExit("ERROR: Some in-text citations do not have matching references.")

    print("Final v3 citation coverage check completed.")


if __name__ == "__main__":
    main()
