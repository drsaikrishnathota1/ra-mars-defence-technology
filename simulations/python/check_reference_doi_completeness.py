"""
Check DOI completeness for final v3 reference list.
"""

import re
from pathlib import Path

REF_FILE = Path("literature-review/reference-list-draft.md")
FINAL_MANUSCRIPT = Path("manuscript/RA-MARS-journal-draft-final-v3.md")

def extract_refs(text):
    return re.findall(r"^\[(\d+)\]\s(.+)$", text, flags=re.MULTILINE)

def main():
    refs_text = REF_FILE.read_text()
    manuscript_text = FINAL_MANUSCRIPT.read_text()

    refs = extract_refs(refs_text)
    manuscript_refs = extract_refs(manuscript_text)

    print(f"References in reference-list-draft.md: {len(refs)}")
    print(f"References in final manuscript: {len(manuscript_refs)}")

    missing_doi = []
    for num, ref in refs:
        if "doi:" not in ref.lower():
            missing_doi.append(num)

    print("References missing DOI:", missing_doi)

    if len(refs) != 43:
        raise SystemExit(f"ERROR: Expected 43 references, found {len(refs)}")

    if missing_doi:
        raise SystemExit("ERROR: Some references are missing DOI.")

    print("All 43 references are present and include DOI fields.")

if __name__ == "__main__":
    main()
