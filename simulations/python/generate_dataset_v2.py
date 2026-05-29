"""
RA-MARS v2 Synthetic UAV Mission Dataset Generator

This version improves the dataset design by using:
- scenario: mission-level scenario
- actual_attack_type: row-level ground-truth label for ML training
- no label confusion between scenario and actual attacked rows
- smaller GitHub-safe sample dataset

This script generates synthetic simulation data only.
It does not represent real military UAV flight data.
"""

import os
import random
import hashlib
from dataclasses import dataclass
from typing import Dict, List

import numpy as np
import pandas as pd


RANDOM_SEED = 42
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)


@dataclass
class SimulationConfig:
    mission_area_m: float = 5000.0
    mission_zones: int = 25
    simulation_duration: int = 300
    telemetry_interval: int = 1
    runs_per_scenario: int = 4
    uav_counts: tuple = (10, 20)
    attack_start: int = 80
    attack_end: int = 240
    attack_probability: float = 0.55


SCENARIOS = ["normal", "jamming", "spoofing", "tampering", "combined"]


def hash_record(record: Dict, previous_hash: str) -> str:
    record_string = (
        f"{record['timestamp']}-{record['run_id']}-{record['uav_id']}-"
        f"{record['x_position']:.3f}-{record['y_position']:.3f}-"
        f"{record['battery_level']:.3f}-{record['mission_progress']:.3f}-"
        f"{previous_hash}"
    )
    return hashlib.sha256(record_string.encode("utf-8")).hexdigest()


def assign_zone(uav_id: int, mission_zones: int) -> int:
    return ((uav_id - 1) % mission_zones) + 1


def risk_level_and_action(risk_score: float):
    if risk_score <= 0.30:
        return "low", "continue"
    if risk_score <= 0.60:
        return "medium", "monitor"
    if risk_score <= 0.80:
        return "high", random.choice(["reroute", "reassign"])
    return "critical", random.choice(["return-to-base", "isolate-node"])


def base_record(
    timestamp: int,
    run_id: int,
    uav_id: int,
    scenario: str,
    config: SimulationConfig,
    previous_hash: str,
) -> Dict:
    expected_x = np.random.uniform(0, config.mission_area_m)
    expected_y = np.random.uniform(0, config.mission_area_m)

    x_position = expected_x + np.random.normal(0, 6)
    y_position = expected_y + np.random.normal(0, 6)

    mission_progress = min(
        100,
        max(0, (timestamp / config.simulation_duration) * 100 + np.random.normal(0, 3)),
    )

    battery_level = max(
        0,
        100 - (timestamp / config.simulation_duration) * np.random.uniform(8, 22),
    )

    record = {
        "timestamp": timestamp,
        "run_id": run_id,
        "uav_id": f"UAV-{uav_id:03d}",
        "scenario": scenario,
        "actual_attack_type": "normal",
        "x_position": x_position,
        "y_position": y_position,
        "expected_x": expected_x,
        "expected_y": expected_y,
        "speed": np.random.uniform(10, 25),
        "battery_level": battery_level,
        "assigned_zone": assign_zone(uav_id, config.mission_zones),
        "mission_progress": mission_progress,
        "packet_delivered": 1,
        "packet_loss_rate": np.random.uniform(0.00, 0.08),
        "latency_ms": np.random.uniform(20, 75),
        "route_deviation": np.random.uniform(0, 15),
        "gps_jump": np.random.uniform(0, 8),
        "velocity_inconsistency": np.random.uniform(0, 3),
        "log_integrity_status": 1,
        "tamper_flag": 0,
        "risk_score": np.random.uniform(0.02, 0.22),
        "risk_level": "low",
        "adaptive_action": "continue",
        "previous_hash": previous_hash,
    }

    record["current_hash"] = hash_record(record, previous_hash)
    return record


def apply_jamming(record: Dict) -> Dict:
    record["actual_attack_type"] = "jamming"
    record["packet_loss_rate"] = np.random.uniform(0.18, 0.58)
    record["packet_delivered"] = 0 if np.random.random() < record["packet_loss_rate"] else 1
    record["latency_ms"] = np.random.uniform(130, 360)
    record["risk_score"] = min(
        1.0,
        0.30 + record["packet_loss_rate"] + np.random.uniform(0.05, 0.18),
    )
    return record


def apply_spoofing(record: Dict) -> Dict:
    record["actual_attack_type"] = "spoofing"
    offset_x = np.random.uniform(40, 320) * random.choice([-1, 1])
    offset_y = np.random.uniform(40, 320) * random.choice([-1, 1])
    record["x_position"] += offset_x
    record["y_position"] += offset_y
    record["route_deviation"] = np.random.uniform(45, 320)
    record["gps_jump"] = np.random.uniform(35, 260)
    record["velocity_inconsistency"] = np.random.uniform(5, 28)
    record["risk_score"] = min(
        1.0,
        0.35 + (record["route_deviation"] / 500) + np.random.uniform(0.05, 0.15),
    )
    return record


def apply_tampering(record: Dict) -> Dict:
    record["actual_attack_type"] = "tampering"
    record["tamper_flag"] = 1
    record["log_integrity_status"] = 0
    record["mission_progress"] = max(
        0,
        min(100, record["mission_progress"] + np.random.uniform(-18, 18)),
    )
    record["risk_score"] = min(1.0, 0.58 + np.random.uniform(0.06, 0.22))
    return record


def apply_combined(record: Dict) -> Dict:
    record = apply_jamming(record)
    record = apply_spoofing(record)
    record = apply_tampering(record)
    record["actual_attack_type"] = "combined"
    record["risk_score"] = min(1.0, 0.82 + np.random.uniform(0.03, 0.12))
    return record


def generate_dataset(config: SimulationConfig) -> pd.DataFrame:
    rows: List[Dict] = []

    for scenario in SCENARIOS:
        for run_id in range(1, config.runs_per_scenario + 1):
            for uav_count in config.uav_counts:
                previous_hash_map = {
                    uav_id: "GENESIS" for uav_id in range(1, uav_count + 1)
                }

                for timestamp in range(
                    0,
                    config.simulation_duration,
                    config.telemetry_interval,
                ):
                    attack_window = config.attack_start <= timestamp <= config.attack_end

                    for uav_id in range(1, uav_count + 1):
                        record = base_record(
                            timestamp=timestamp,
                            run_id=run_id,
                            uav_id=uav_id,
                            scenario=scenario,
                            config=config,
                            previous_hash=previous_hash_map[uav_id],
                        )

                        affected = attack_window and np.random.random() < config.attack_probability

                        if scenario != "normal" and affected:
                            if scenario == "jamming":
                                record = apply_jamming(record)
                            elif scenario == "spoofing":
                                record = apply_spoofing(record)
                            elif scenario == "tampering":
                                record = apply_tampering(record)
                            elif scenario == "combined":
                                record = apply_combined(record)

                        record["risk_level"], record["adaptive_action"] = risk_level_and_action(
                            record["risk_score"]
                        )
                        record["current_hash"] = hash_record(record, record["previous_hash"])
                        previous_hash_map[uav_id] = record["current_hash"]

                        rows.append(record)

    return pd.DataFrame(rows)


def main() -> None:
    config = SimulationConfig()
    df = generate_dataset(config)

    output_dir = "simulations/datasets"
    os.makedirs(output_dir, exist_ok=True)

    full_path = os.path.join(output_dir, "synthetic_uav_mission_data_v2_full.csv")
    sample_path = os.path.join(output_dir, "synthetic_uav_mission_data_v2_sample.csv")
    summary_path = os.path.join(output_dir, "dataset_summary_v2.csv")
    class_path = os.path.join(output_dir, "class_distribution_v2.csv")

    df.to_csv(full_path, index=False)

    sample_size = min(50000, len(df))
    sample_df = df.sample(n=sample_size, random_state=RANDOM_SEED)
    sample_df.to_csv(sample_path, index=False)

    summary = df.groupby(["scenario", "actual_attack_type"]).agg(
        records=("actual_attack_type", "count"),
        avg_risk_score=("risk_score", "mean"),
        avg_latency_ms=("latency_ms", "mean"),
        avg_packet_loss_rate=("packet_loss_rate", "mean"),
        avg_route_deviation=("route_deviation", "mean"),
        tamper_rate=("tamper_flag", "mean"),
    )
    summary.to_csv(summary_path)

    df["actual_attack_type"].value_counts().to_csv(class_path)

    print(f"Generated full dataset: {full_path}")
    print(f"Generated GitHub-safe sample: {sample_path}")
    print(f"Generated summary: {summary_path}")
    print(f"Generated class distribution: {class_path}")
    print(f"Total full records: {len(df):,}")
    print(f"Sample records: {len(sample_df):,}")


if __name__ == "__main__":
    main()
