"""
Fast RunPod patch for RA-MARS v3.

This avoids huge full CSV files and creates only a sequence-safe sample.
"""

from pathlib import Path
import re

p = Path("simulations/python/generate_dataset_v3.py")
text = p.read_text()

text = re.sub(r"simulation_duration: int = \d+", "simulation_duration: int = 240", text)
text = re.sub(
    r"seeds: tuple = tuple\(range\(1, \d+\)\).*",
    "seeds: tuple = tuple(range(1, 9))   # fast RunPod: 8 seeds",
    text,
)
text = re.sub(
    r"uav_counts: tuple = .*",
    "uav_counts: tuple = (10, 20, 30)   # fast RunPod: 3 swarm sizes",
    text,
)
text = re.sub(r"attack_start: int = \d+", "attack_start: int = 60", text)
text = re.sub(r"attack_end: int = \d+", "attack_end: int = 180", text)

# Disable full CSV save
text = text.replace(
    "    df.to_csv(full_path, index=False)\n",
    "    print('Skipping full CSV save to avoid huge files.')\n",
)

# Replace random row sampling with sequence-safe complete group sampling
old_pattern = re.compile(
    r"    sample_size = min\(\d+, len\(df\)\)\n"
    r"    sample_df = df\.sample\(n=sample_size, random_state=RANDOM_SEED\)\n"
    r"    sample_df\.to_csv\(sample_path, index=False\)\n",
    re.MULTILINE,
)

new_block = '''    # Sequence-safe sampling: select complete UAV time-series groups.
    target_sample_size = min(90000, len(df))
    group_cols = ["seed", "scenario", "attack_intensity", "uav_count", "uav_id"]

    group_keys = list(df.groupby(group_cols).groups.keys())
    random.Random(RANDOM_SEED).shuffle(group_keys)

    sampled_groups = []
    sampled_rows = 0

    for key in group_keys:
        group_df = df[
            (df["seed"] == key[0]) &
            (df["scenario"] == key[1]) &
            (df["attack_intensity"] == key[2]) &
            (df["uav_count"] == key[3]) &
            (df["uav_id"] == key[4])
        ].sort_values("timestamp")

        sampled_groups.append(group_df)
        sampled_rows += len(group_df)

        if sampled_rows >= target_sample_size:
            break

    sample_df = pd.concat(sampled_groups, ignore_index=True)
    sample_df.to_csv(sample_path, index=False)
'''

if old_pattern.search(text):
    text = old_pattern.sub(new_block, text)
elif "target_sample_size" not in text:
    raise SystemExit("Sampling block not found. Stop and ask ChatGPT.")

text = text.replace(
    'print(f"Generated full v3 dataset: {full_path}")',
    'print("Full v3 dataset was not saved by fast RunPod configuration.")',
)

p.write_text(text)
print("Applied fast RunPod v3 patch.")
