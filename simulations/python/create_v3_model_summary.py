"""
Create combined RA-MARS v3 model summary table.
Combines classical, unweighted sequence, and weighted sequence results.
"""

from pathlib import Path
import pandas as pd

RESULTS_DIR = Path("simulations/results")
OUT = RESULTS_DIR / "model_performance_v3_combined_summary.csv"

files = [
    RESULTS_DIR / "model_performance_v3_classical.csv",
    RESULTS_DIR / "model_performance_v3_sequence.csv",
    RESULTS_DIR / "model_performance_v3_sequence_weighted.csv",
]

dfs = []
for f in files:
    if f.exists():
        df = pd.read_csv(f)
        df["source_file"] = f.name
        dfs.append(df)

combined = pd.concat(dfs, ignore_index=True)
combined = combined.sort_values("f1_macro", ascending=False)

combined.to_csv(OUT, index=False)

print(f"Saved combined v3 model summary: {OUT}")
print(combined.to_string(index=False))
