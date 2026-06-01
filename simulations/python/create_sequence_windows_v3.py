"""
RA-MARS v3 Sequence Window Builder

Converts row-level UAV telemetry into fixed-length time-series windows.

Input:
- simulations/datasets/uav_mission_telemetry_v3_sample.csv

Output:
- simulations/datasets/uav_sequence_windows_v3.npz
- simulations/datasets/sequence_label_distribution_v3.csv

Each sample is a telemetry window for one UAV:
shape = (window_size, number_of_features)
"""

import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


DATA_PATH = "simulations/datasets/uav_mission_telemetry_v3_sample.csv"
OUTPUT_PATH = "simulations/datasets/uav_sequence_windows_v3.npz"
LABEL_DISTRIBUTION_PATH = "simulations/datasets/sequence_label_distribution_v3.csv"

WINDOW_SIZE = 20
STRIDE = 5

FEATURES = [
    "packet_loss_rate",
    "latency_ms",
    "route_deviation",
    "gps_jump",
    "velocity_inconsistency",
    "battery_level",
    "mission_progress",
    "zone_coverage",
    "energy_consumption",
    "mission_assurance_index",
    "communication_score",
    "navigation_score",
    "coverage_score",
    "integrity_score",
    "recovery_score",
]


def load_data():
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(
            f"Dataset not found: {DATA_PATH}. Run generate_dataset_v3.py first."
        )

    df = pd.read_csv(DATA_PATH)

    required = FEATURES + [
        "seed",
        "scenario",
        "attack_intensity",
        "uav_count",
        "uav_id",
        "timestamp",
        "actual_attack_type",
    ]

    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    return df


def build_windows(df):
    X_windows = []
    y_labels = []
    meta_rows = []

    group_cols = ["seed", "scenario", "attack_intensity", "uav_count", "uav_id"]

    for group_key, group in df.groupby(group_cols):
        group = group.sort_values("timestamp").reset_index(drop=True)

        if len(group) < WINDOW_SIZE:
            continue

        values = group[FEATURES].values
        labels = group["actual_attack_type"].values
        timestamps = group["timestamp"].values

        for start in range(0, len(group) - WINDOW_SIZE + 1, STRIDE):
            end = start + WINDOW_SIZE

            window = values[start:end]
            label_window = labels[start:end]

            # Use majority label inside the window.
            unique, counts = np.unique(label_window, return_counts=True)
            majority_label = unique[np.argmax(counts)]

            # If any attack exists and normal is only a weak majority, prefer attack label.
            if majority_label == "normal":
                attack_labels = label_window[label_window != "normal"]
                if len(attack_labels) >= WINDOW_SIZE * 0.30:
                    unique_a, counts_a = np.unique(attack_labels, return_counts=True)
                    majority_label = unique_a[np.argmax(counts_a)]

            X_windows.append(window)
            y_labels.append(majority_label)

            meta_rows.append({
                "seed": group_key[0],
                "scenario": group_key[1],
                "attack_intensity": group_key[2],
                "uav_count": group_key[3],
                "uav_id": group_key[4],
                "start_timestamp": int(timestamps[start]),
                "end_timestamp": int(timestamps[end - 1]),
                "label": majority_label,
            })

    X = np.array(X_windows, dtype=np.float32)
    y = np.array(y_labels)

    meta = pd.DataFrame(meta_rows)

    return X, y, meta


def encode_labels(y):
    label_names = sorted(np.unique(y).tolist())
    label_to_id = {label: idx for idx, label in enumerate(label_names)}
    y_encoded = np.array([label_to_id[label] for label in y], dtype=np.int64)
    return y_encoded, label_names


def scale_windows(X):
    n_samples, window_size, n_features = X.shape
    flat = X.reshape(-1, n_features)

    scaler = StandardScaler()
    flat_scaled = scaler.fit_transform(flat)

    X_scaled = flat_scaled.reshape(n_samples, window_size, n_features).astype(np.float32)
    return X_scaled


def main():
    df = load_data()

    X, y, meta = build_windows(df)

    if len(X) == 0:
        raise RuntimeError("No sequence windows generated. Check dataset and window size.")

    X_scaled = scale_windows(X)
    y_encoded, label_names = encode_labels(y)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    np.savez_compressed(
        OUTPUT_PATH,
        X=X_scaled,
        y=y_encoded,
        labels=np.array(label_names),
    )

    label_dist = pd.Series(y).value_counts().rename_axis("label").reset_index(name="count")
    label_dist.to_csv(LABEL_DISTRIBUTION_PATH, index=False)

    meta_path = "simulations/datasets/sequence_metadata_v3.csv"
    meta.to_csv(meta_path, index=False)

    print(f"Generated sequence windows: {OUTPUT_PATH}")
    print(f"Generated label distribution: {LABEL_DISTRIBUTION_PATH}")
    print(f"Generated sequence metadata: {meta_path}")
    print(f"X shape: {X_scaled.shape}")
    print(f"y shape: {y_encoded.shape}")
    print("Labels:", label_names)
    print("Label distribution:")
    print(label_dist.to_string(index=False))


if __name__ == "__main__":
    main()
