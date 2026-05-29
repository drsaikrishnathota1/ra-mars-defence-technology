"""
RA-MARS Synthetic UAV Mission Dataset Generator

This script generates synthetic multi-UAV telemetry data for evaluating
RA-MARS: Resilient AI-Driven Mission Assurance for Secure Multi-UAV Defence Surveillance.

Scenarios:
1. Normal operation
2. RF jamming
3. GPS/GNSS spoofing
4. Mission-data tampering
5. Combined attack
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
    mission_area_km: float = 5.0
    mission_zones: int = 25
    simulation_duration: int = 600
    telemetry_interval: int = 1
    runs_per_scenario: int = 5
    uav_counts: tuple = (10, 20, 30)


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
    return (uav_id % mission_zones) + 1


def generate_base_telemetry(
    timestamp: int,
    run_id: int,
    uav_id: int,
    scenario: str,
    config: SimulationConfig,
    previous_hash: str,
) -> Dict:
    mission_area_m = config.mission_area_km * 1000

    expected_x = np.random.uniform(0, mission_area_m)
    expected_y = np.random.uniform(0, mission_area_m)

    x_position = expected_x + np.random.normal(0, 5)
    y_position = expected_y + np.random.normal(0, 5)

    speed = np.random.uniform(10, 25)
    battery_level = max(
        0,
        100 - (timestamp / config.simulation_duration) * np.random.uniform(10, 25),
    )
    assigned_zone = assign_zone(uav_id, config.mission_zones)
    mission_progress = min(
        100,
        (timestamp / config.simulation_duration) * 100 + np.random.normal(0, 2),
    )

    record = {
        "timestamp": timestamp,
        "run_id": run_id,
        "uav_id": f"UAV-{uav_id:03d}",
        "scenario": scenario,
        "x_position": x_position,
        "y_position": y_position,
        "expected_x": expected_x,
        "expected_y": expected_y,
        "speed": speed,
        "battery_level": battery_level,
        "assigned_zone": assigned_zone,
        "mission_progress": mission_progress,
        "packet_delivered": 1,
        "packet_loss_rate": np.random.uniform(0.00, 0.05),
        "latency_ms": np.random.uniform(20, 60),
        "route_deviation": np.random.uniform(0, 10),
        "gps_jump": np.random.uniform(0, 5),
        "velocity_inconsistency": np.random.uniform(0, 2),
        "log_integrity_status": 1,
        "tamper_flag": 0,
        "attack_probability": np.random.uniform(0.00, 0.10),
        "risk_score": np.random.uniform(0.00, 0.20),
        "risk_level": "low",
        "adaptive_action": "continue",
        "previous_hash": previous_hash,
        "label": scenario,
    }

    record["current_hash"] = hash_record(record, previous_hash)
    return record


def apply_jamming(record: Dict) -> Dict:
    record["packet_loss_rate"] = np.random.uniform(0.20, 0.60)
    record["packet_delivered"] = 0 if np.random.random() < record["packet_loss_rate"] else 1
    record["latency_ms"] += np.random.uniform(50, 300)
    record["attack_probability"] = np.random.uniform(0.65, 0.95)
    record["risk_score"] = min(
        1.0,
        0.30 + record["packet_loss_rate"] + np.random.uniform(0.05, 0.15),
    )
    return record


def apply_spoofing(record: Dict) -> Dict:
    spoof_offset_x = np.random.uniform(20, 300) * random.choice([-1, 1])
    spoof_offset_y = np.random.uniform(20, 300) * random.choice([-1, 1])

    record["x_position"] += spoof_offset_x
    record["y_position"] += spoof_offset_y
    record["route_deviation"] = np.random.uniform(50, 300)
    record["gps_jump"] = np.random.uniform(30, 250)
    record["velocity_inconsistency"] = np.random.uniform(5, 25)
    record["attack_probability"] = np.random.uniform(0.65, 0.95)
    record["risk_score"] = min(
        1.0,
        0.40 + (record["route_deviation"] / 500) + np.random.uniform(0.05, 0.15),
    )
    return record


def apply_tampering(record: Dict) -> Dict:
    record["tamper_flag"] = 1
    record["log_integrity_status"] = 0
    record["mission_progress"] = max(
        0,
        min(100, record["mission_progress"] + np.random.uniform(-20, 20)),
    )
    record["attack_probability"] = np.random.uniform(0.65, 0.95)
    record["risk_score"] = min(1.0, 0.55 + np.random.uniform(0.10, 0.25))
    return record


def assign_risk_action(record: Dict) -> Dict:
    risk = record["risk_score"]

    if risk <= 0.30:
        record["risk_level"] = "low"
        record["adaptive_action"] = "continue"
    elif risk <= 0.60:
        record["risk_level"] = "medium"
        record["adaptive_action"] = "monitor"
    elif risk <= 0.80:
        record["risk_level"] = "high"
        record["adaptive_action"] = random.choice(["reroute", "reassign"])
    else:
        record["risk_level"] = "critical"
        record["adaptive_action"] = random.choice(["return-to-base", "isolate-node"])

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
                    attack_active = 150 <= timestamp <= 450

                    for uav_id in range(1, uav_count + 1):
                        record = generate_base_telemetry(
                            timestamp=timestamp,
                            run_id=run_id,
                            uav_id=uav_id,
                            scenario=scenario,
                            config=config,
                            previous_hash=previous_hash_map[uav_id],
                        )

                        affected = attack_active and (np.random.random() < 0.45)

                        if affected:
                            if scenario == "jamming":
                                record = apply_jamming(record)
                            elif scenario == "spoofing":
                                record = apply_spoofing(record)
                            elif scenario == "tampering":
                                record = apply_tampering(record)
                            elif scenario == "combined":
                                record = apply_jamming(record)
                                record = apply_spoofing(record)
                                record = apply_tampering(record)

                        record = assign_risk_action(record)
                        record["current_hash"] = hash_record(record, record["previous_hash"])
                        previous_hash_map[uav_id] = record["current_hash"]

                        rows.append(record)

    return pd.DataFrame(rows)


def main() -> None:
    config = SimulationConfig()
    df = generate_dataset(config)

    output_dir = "simulations/datasets"
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "synthetic_uav_mission_data.csv")
    df.to_csv(output_path, index=False)

    summary_path = os.path.join(output_dir, "dataset_summary.csv")
    summary = df.groupby("scenario").agg(
        records=("scenario", "count"),
        avg_risk_score=("risk_score", "mean"),
        avg_latency_ms=("latency_ms", "mean"),
        avg_packet_loss_rate=("packet_loss_rate", "mean"),
        avg_route_deviation=("route_deviation", "mean"),
        tamper_rate=("tamper_flag", "mean"),
    )
    summary.to_csv(summary_path)

    class_distribution_path = os.path.join(output_dir, "class_distribution.csv")
    df["label"].value_counts().to_csv(class_distribution_path)

    print(f"Generated dataset: {output_path}")
    print(f"Generated summary: {summary_path}")
    print(f"Generated class distribution: {class_distribution_path}")
    print(f"Total records: {len(df):,}")


if __name__ == "__main__":
    main()