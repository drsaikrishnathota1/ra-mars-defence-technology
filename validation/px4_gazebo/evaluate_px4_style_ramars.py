"""
RA-MARS evaluator for PX4/Gazebo-style telemetry.

Inputs:
- validation/px4_gazebo/data/px4_style_mavlink_telemetry.csv
- validation/px4_gazebo/data/px4_style_mavlink_telemetry_tampered.csv

Outputs:
- mission assurance summary
- attack timeline summary
- tamper verification summary
- validation figures
"""

from pathlib import Path
import hashlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


DATA_DIR = Path("validation/px4_gazebo/data")
RESULT_DIR = Path("validation/px4_gazebo/results")
FIG_DIR = Path("validation/px4_gazebo/figures")

RESULT_DIR.mkdir(parents=True, exist_ok=True)
FIG_DIR.mkdir(parents=True, exist_ok=True)


RAW_FILE = DATA_DIR / "px4_style_mavlink_telemetry.csv"
TAMPERED_FILE = DATA_DIR / "px4_style_mavlink_telemetry_tampered.csv"


def recompute_hash(row, previous_hash):
    excluded = {"previous_hash", "record_hash"}
    row_dict = {k: row[k] for k in row.index if k not in excluded}
    payload = "|".join(str(row_dict[k]) for k in sorted(row_dict.keys()))
    payload = previous_hash + "|" + payload
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def classify_predicted_attack(row):
    if row["packet_received"] == 0 or row["latency_ms"] > 100:
        if row["gps_drift_m"] > 20 or row["route_deviation_m"] > 25:
            return "combined"
        return "jamming"

    if row["gps_drift_m"] > 15 or row["route_deviation_m"] > 25:
        return "spoofing"

    if row["tamper_flag"] == 1:
        return "tampering"

    return "normal"


def compute_mission_assurance(row):
    packet_score = 1.0 if row["packet_received"] == 1 else 0.35
    latency_score = max(0.0, 1.0 - row["latency_ms"] / 220.0)
    nav_score = max(0.0, 1.0 - row["route_deviation_m"] / 80.0)
    gps_score = max(0.0, 1.0 - row["gps_drift_m"] / 70.0)
    battery_score = max(0.0, min(1.0, row["battery"] / 100.0))
    progress_score = max(0.0, min(1.0, row["mission_progress"] / 100.0))
    integrity_score = 0.4 if row["tamper_flag"] == 1 else 1.0

    mai = (
        0.18 * packet_score
        + 0.14 * latency_score
        + 0.18 * nav_score
        + 0.14 * gps_score
        + 0.10 * battery_score
        + 0.12 * progress_score
        + 0.14 * integrity_score
    )
    return max(0.0, min(1.0, mai))


def action_from_mai(mai, predicted_attack):
    if mai >= 0.78 and predicted_attack == "normal":
        return "continue"
    if mai >= 0.68:
        return "monitor"
    if predicted_attack == "jamming":
        return "reroute"
    if predicted_attack == "spoofing":
        return "reassign"
    if predicted_attack == "tampering":
        return "isolate_node"
    if predicted_attack == "combined":
        return "reassign_and_isolate"
    return "return_to_base"


def verify_hash_chain(tampered_df):
    mismatches = []

    for uav_id, group in tampered_df.groupby("uav_id"):
        group = group.sort_values("timestamp")
        expected_previous = "GENESIS"

        for idx, row in group.iterrows():
            expected_hash = recompute_hash(row, expected_previous)
            if row["previous_hash"] != expected_previous or row["record_hash"] != expected_hash:
                mismatches.append(
                    {
                        "row_index": idx,
                        "uav_id": uav_id,
                        "timestamp": row["timestamp"],
                        "attack_type": row["attack_type"],
                    }
                )
            expected_previous = row["record_hash"]

    return pd.DataFrame(mismatches)


def make_figures(df):
    # Figure 1: trajectory
    fig, ax = plt.subplots(figsize=(8, 6))
    for uav_id, group in df.groupby("uav_id"):
        ax.plot(group["local_x"], group["local_y"], label=f"UAV {uav_id}")
    ax.set_title("PX4-Style Multi-UAV Mission Trajectories")
    ax.set_xlabel("Local X Position (m)")
    ax.set_ylabel("Local Y Position (m)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIG_DIR / "px4_style_mission_trajectories.png", dpi=300)
    fig.savefig(FIG_DIR / "px4_style_mission_trajectories.pdf")
    plt.close(fig)

    # Figure 2: Mission Assurance Index over time
    fig, ax = plt.subplots(figsize=(9, 5))
    grouped = df.groupby("timestamp")["mission_assurance_index"].mean()
    ax.plot(grouped.index, grouped.values)
    ax.set_title("RA-MARS Mission Assurance Index on PX4-Style Telemetry")
    ax.set_xlabel("Mission Time (s)")
    ax.set_ylabel("Mean Mission Assurance Index")
    fig.tight_layout()
    fig.savefig(FIG_DIR / "px4_style_mission_assurance_index.png", dpi=300)
    fig.savefig(FIG_DIR / "px4_style_mission_assurance_index.pdf")
    plt.close(fig)

    # Figure 3: attack timeline counts
    counts = df.groupby(["timestamp", "attack_type"]).size().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=(9, 5))
    for col in counts.columns:
        ax.plot(counts.index, counts[col], label=col)
    ax.set_title("PX4-Style Attack Timeline")
    ax.set_xlabel("Mission Time (s)")
    ax.set_ylabel("Number of UAV Telemetry Records")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIG_DIR / "px4_style_attack_timeline.png", dpi=300)
    fig.savefig(FIG_DIR / "px4_style_attack_timeline.pdf")
    plt.close(fig)

    # Figure 4: action distribution
    action_counts = df["selected_action"].value_counts()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(action_counts.index, action_counts.values)
    ax.set_title("RA-MARS Digital Twin Action Selection on PX4-Style Telemetry")
    ax.set_xlabel("Selected Action")
    ax.set_ylabel("Count")
    ax.tick_params(axis="x", rotation=30)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "px4_style_action_selection.png", dpi=300)
    fig.savefig(FIG_DIR / "px4_style_action_selection.pdf")
    plt.close(fig)


def main():
    raw = pd.read_csv(RAW_FILE)
    tampered = pd.read_csv(TAMPERED_FILE)

    df = raw.copy()
    df["predicted_attack"] = df.apply(classify_predicted_attack, axis=1)
    df["mission_assurance_index"] = df.apply(compute_mission_assurance, axis=1)
    df["selected_action"] = df.apply(
        lambda row: action_from_mai(row["mission_assurance_index"], row["predicted_attack"]),
        axis=1,
    )

    mission_success_rate = float((df["mission_assurance_index"] >= 0.65).mean() * 100)
    mean_mai = float(df["mission_assurance_index"].mean())
    mean_pdr = float(df["packet_received"].mean())
    mean_latency = float(df["latency_ms"].mean())
    mean_route_deviation = float(df["route_deviation_m"].mean())
    mean_gps_drift = float(df["gps_drift_m"].mean())

    tamper_mismatches = verify_hash_chain(tampered)
    tamper_detection_rate = 0.0
    if int(df["tamper_flag"].sum()) > 0:
        tamper_detection_rate = min(100.0, len(tamper_mismatches) / int(df["tamper_flag"].sum()) * 100)

    summary = pd.DataFrame(
        [
            {
                "validation_type": "PX4-style MAVLink telemetry emulation",
                "uav_count": df["uav_id"].nunique(),
                "telemetry_rows": len(df),
                "mission_success_rate": mission_success_rate,
                "mission_assurance_index_mean": mean_mai,
                "packet_delivery_ratio": mean_pdr,
                "latency_ms_mean": mean_latency,
                "route_deviation_m_mean": mean_route_deviation,
                "gps_drift_m_mean": mean_gps_drift,
                "tamper_mismatches_detected": len(tamper_mismatches),
                "tamper_detection_rate_proxy": tamper_detection_rate,
            }
        ]
    )

    attack_summary = (
        df.groupby("attack_type")
        .agg(
            rows=("timestamp", "count"),
            mean_mai=("mission_assurance_index", "mean"),
            pdr=("packet_received", "mean"),
            latency_ms=("latency_ms", "mean"),
            route_deviation_m=("route_deviation_m", "mean"),
            gps_drift_m=("gps_drift_m", "mean"),
        )
        .reset_index()
    )

    action_summary = df["selected_action"].value_counts().rename_axis("action").reset_index(name="count")

    df.to_csv(RESULT_DIR / "px4_style_ramars_scored_telemetry.csv", index=False)
    summary.to_csv(RESULT_DIR / "px4_style_validation_summary.csv", index=False)
    attack_summary.to_csv(RESULT_DIR / "px4_style_attack_summary.csv", index=False)
    action_summary.to_csv(RESULT_DIR / "px4_style_action_summary.csv", index=False)
    tamper_mismatches.to_csv(RESULT_DIR / "px4_style_tamper_verification.csv", index=False)

    make_figures(df)

    print("Saved RA-MARS PX4-style validation results.")
    print(summary.to_string(index=False))
    print("\nAttack summary:")
    print(attack_summary.to_string(index=False))
    print("\nAction summary:")
    print(action_summary.to_string(index=False))
    print("\nTamper mismatches detected:", len(tamper_mismatches))


if __name__ == "__main__":
    main()
