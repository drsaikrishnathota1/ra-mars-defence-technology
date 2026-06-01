"""
Patch RA-MARS v3 dataset generator for full RunPod-scale execution.
"""

from pathlib import Path

p = Path("simulations/python/generate_dataset_v3.py")
text = p.read_text()

replacements = {
    "simulation_duration: int = 180": "simulation_duration: int = 360",
    "seeds: tuple = tuple(range(1, 4))   # local-safe: 3 seeds; RunPod can expand to 30": "seeds: tuple = tuple(range(1, 31))   # RunPod full-scale: 30 seeds",
    "uav_counts: tuple = (10, 20)   # local-safe; RunPod can use 10,20,30,50": "uav_counts: tuple = (10, 20, 30, 50)   # RunPod full-scale",
    "attack_start: int = 45": "attack_start: int = 90",
    "attack_end: int = 135": "attack_end: int = 270",
    "sample_size = min(40000, len(df))": "sample_size = min(120000, len(df))",
}

for old, new in replacements.items():
    if old not in text:
        print(f"Warning: pattern not found: {old}")
    text = text.replace(old, new)

p.write_text(text)
print("Patched generate_dataset_v3.py for RunPod full-scale execution.")
