"""
RA-MARS v3 Synthetic Multi-UAV Mission Dataset Generator

v3 upgrades:
- multiple UAV swarm sizes
- multiple random seeds
- low/medium/high attack intensities
- adaptive jamming, spoofing, tampering, and combined attacks
- mission assurance index
- digital-twin action candidates
- row-level attack labels
- GitHub-safe sample output

This dataset is synthetic simulation data only.
It does not represent real military UAV flight data.
"""

import os
import random
import hashlib
from dataclasses import dataclass
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd


RANDOM_SEED = 42
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)


@dataclass
class V3Config:
    mission_area_m: float = 5000.0
    mission_zones: int = 25
    simulation_duration: int = 180
    telemetry_interval: int = 1
    seeds: tuple = tuple(range(1, 4))   # local-safe: 3 seeds; RunPod can expand to 30
    uav_counts: tuple = (10, 20)   # local-safe; RunPod can use 10,20,30,50
    attack_start: int = 45
    attack_end: int = 135


SCENARIOS = [
    "normal",
    "jamming",
    "spoofing",
    "tampering",
    "jamming_spoofing",
    "spoofing_tampering",
    "jamming_tampering",
    "combined",
]

ATTACK_INTENSITIES = ["low", "medium", "high"]

JAMMING_TYPES = ["barrage", "intermittent", "reactive", "adaptive"]
SPOOFING_TYPES = ["sudden_jump", "gradual_drift", "coordinated_swarm"]
TAMPERING_TYPES = ["position_tampering", "timestamp_tampering", "mission_progress_tampering", "selective_log_tampering"]

ACTIONS = ["continue", "monitor", "reroute", "reassign", "isolate-node", "return-to-base"]


def intensity_factor(intensity: str) -> float:
    return {"low": 0.65, "medium": 1.0, "high": 1.35}[intensity]


def attack_probability(intensity: str) -> float:
    return {"low": 0.35, "medium": 0.55, "high": 0.75}[intensity]


def hash_record(record: Dict, previous_hash: str) -> str:
    record_string = (
        f"{record['seed']}-{record['timestamp']}-{record['run_id']}-{record['uav_id']}-"
        f"{record['x_position']:.3f}-{record['y_position']:.3f}-"
        f"{record['battery_level']:.3f}-{record['mission_progress']:.3f}-"
        f"{record['actual_attack_type']}-{previous_hash}"
    )
    return hashlib.sha256(record_string.encode("utf-8")).hexdigest()


def assign_zone(uav_id: int, mission_zones: int) -> int:
    return ((uav_id - 1) % mission_zones) + 1


def base_record(
    seed: int,
    timestamp: int,
    run_id: int,
    uav_id: int,
    uav_count: int,
    scenario: str,
    intensity: str,
    config: V3Config,
    previous_hash: str,
) -> Dict:
    expected_x = np.random.uniform(0, config.mission_area_m)
    expected_y = np.random.uniform(0, config.mission_area_m)

    x_position = expected_x + np.random.normal(0, 5)
    y_position = expected_y + np.random.normal(0, 5)

    mission_progress = min(
        100,
        max(0, (timestamp / config.simulation_duration) * 100 + np.random.normal(0, 2.5)),
    )

    battery_level = max(
        0,
        100 - (timestamp / config.simulation_duration) * np.random.uniform(8, 24),
    )

    record = {
        "seed": seed,
        "timestamp": timestamp,
        "run_id": run_id,
        "uav_count": uav_count,
        "uav_id": f"UAV-{uav_id:03d}",
        "scenario": scenario,
        "attack_intensity": intensity,
        "actual_attack_type": "normal",
        "jamming_type": "none",
        "spoofing_type": "none",
        "tampering_type": "none",
        "x_position": x_position,
        "y_position": y_position,
        "expected_x": expected_x,
        "expected_y": expected_y,
        "speed": np.random.uniform(10, 25),
        "battery_level": battery_level,
        "assigned_zone": assign_zone(uav_id, config.mission_zones),
        "mission_progress": mission_progress,
        "zone_coverage": min(100, max(0, mission_progress + np.random.normal(0, 4))),
        "packet_delivered": 1,
        "packet_loss_rate": np.random.uniform(0.00, 0.06),
        "latency_ms": np.random.uniform(20, 70),
        "route_deviation": np.random.uniform(0, 12),
        "gps_jump": np.random.uniform(0, 6),
        "velocity_inconsistency": np.random.uniform(0, 2.5),
        "log_integrity_status": 1,
        "tamper_flag": 0,
        "energy_consumption": np.random.uniform(0.02, 0.08),
        "detection_delay_sec": 0,
        "false_alarm_flag": 0,
        "previous_hash": previous_hash,
    }

    return record


def apply_jamming(record: Dict, intensity: str, timestamp: int) -> Dict:
    f = intensity_factor(intensity)
    j_type = random.choice(JAMMING_TYPES)

    record["actual_attack_type"] = "jamming"
    record["jamming_type"] = j_type

    if j_type == "barrage":
        loss = np.random.uniform(0.18, 0.42) * f
        latency = np.random.uniform(120, 260) * f
    elif j_type == "intermittent":
        active = (timestamp // 15) % 2 == 0
        loss = np.random.uniform(0.05, 0.16) if not active else np.random.uniform(0.20, 0.50) * f
        latency = np.random.uniform(70, 130) if not active else np.random.uniform(140, 310) * f
    elif j_type == "reactive":
        loss = np.random.uniform(0.12, 0.36) * f
        latency = np.random.uniform(100, 280) * f
    else:  # adaptive
        ramp = min(1.0, max(0.15, (timestamp - 90) / 180))
        loss = np.random.uniform(0.12, 0.40) * f * ramp
        latency = np.random.uniform(100, 300) * f * ramp

    record["packet_loss_rate"] = min(0.95, loss)
    record["packet_delivered"] = 0 if np.random.random() < record["packet_loss_rate"] else 1
    record["latency_ms"] = min(700, latency)
    record["energy_consumption"] += np.random.uniform(0.02, 0.07) * f
    return record


def apply_spoofing(record: Dict, intensity: str, timestamp: int, uav_id: int) -> Dict:
    f = intensity_factor(intensity)
    s_type = random.choice(SPOOFING_TYPES)

    record["actual_attack_type"] = "spoofing"
    record["spoofing_type"] = s_type

    if s_type == "sudden_jump":
        offset_x = np.random.uniform(40, 280) * f * random.choice([-1, 1])
        offset_y = np.random.uniform(40, 280) * f * random.choice([-1, 1])
    elif s_type == "gradual_drift":
        drift = min(1.0, max(0.1, (timestamp - 90) / 180))
        offset_x = np.random.uniform(20, 220) * f * drift * random.choice([-1, 1])
        offset_y = np.random.uniform(20, 220) * f * drift * random.choice([-1, 1])
    else:  # coordinated_swarm
        direction = 1 if uav_id % 2 == 0 else -1
        offset_x = np.random.uniform(60, 260) * f * direction
        offset_y = np.random.uniform(60, 260) * f * direction

    record["x_position"] += offset_x
    record["y_position"] += offset_y
    record["route_deviation"] = min(600, np.random.uniform(35, 260) * f)
    record["gps_jump"] = min(500, np.random.uniform(30, 220) * f)
    record["velocity_inconsistency"] = min(60, np.random.uniform(4, 24) * f)
    record["zone_coverage"] = max(0, record["zone_coverage"] - np.random.uniform(5, 20) * f)
    return record


def apply_tampering(record: Dict, intensity: str) -> Dict:
    f = intensity_factor(intensity)
    t_type = random.choice(TAMPERING_TYPES)

    record["actual_attack_type"] = "tampering"
    record["tampering_type"] = t_type
    record["tamper_flag"] = 1
    record["log_integrity_status"] = 0

    if t_type == "position_tampering":
        record["x_position"] += np.random.uniform(-150, 150) * f
        record["y_position"] += np.random.uniform(-150, 150) * f
    elif t_type == "timestamp_tampering":
        record["timestamp"] = max(0, int(record["timestamp"] + np.random.randint(-20, 20) * f))
    elif t_type == "mission_progress_tampering":
        record["mission_progress"] = max(0, min(100, record["mission_progress"] + np.random.uniform(-25, 25) * f))
    else:
        record["log_integrity_status"] = 0

    return record


def apply_attack(record: Dict, scenario: str, intensity: str, timestamp: int, uav_id: int) -> Dict:
    if scenario == "jamming":
        return apply_jamming(record, intensity, timestamp)
    if scenario == "spoofing":
        return apply_spoofing(record, intensity, timestamp, uav_id)
    if scenario == "tampering":
        return apply_tampering(record, intensity)
    if scenario == "jamming_spoofing":
        record = apply_jamming(record, intensity, timestamp)
        record = apply_spoofing(record, intensity, timestamp, uav_id)
        record["actual_attack_type"] = "jamming_spoofing"
        return record
    if scenario == "spoofing_tampering":
        record = apply_spoofing(record, intensity, timestamp, uav_id)
        record = apply_tampering(record, intensity)
        record["actual_attack_type"] = "spoofing_tampering"
        return record
    if scenario == "jamming_tampering":
        record = apply_jamming(record, intensity, timestamp)
        record = apply_tampering(record, intensity)
        record["actual_attack_type"] = "jamming_tampering"
        return record
    if scenario == "combined":
        record = apply_jamming(record, intensity, timestamp)
        record = apply_spoofing(record, intensity, timestamp, uav_id)
        record = apply_tampering(record, intensity)
        record["actual_attack_type"] = "combined"
        return record
    return record


def compute_mission_assurance(record: Dict) -> Tuple[float, float, float, float, float, float]:
    comm = max(0, min(1, 0.65 * (1 - record["packet_loss_rate"]) + 0.35 * (1 - min(record["latency_ms"], 500) / 500)))
    nav = max(0, min(1, 0.50 * (1 - min(record["route_deviation"], 400) / 400) + 0.30 * (1 - min(record["gps_jump"], 300) / 300) + 0.20 * (1 - min(record["velocity_inconsistency"], 40) / 40)))
    coverage = max(0, min(1, record["zone_coverage"] / 100))
    integrity = 1.0 if record["log_integrity_status"] == 1 else 0.0
    recovery = max(0, min(1, 1 - record["detection_delay_sec"] / 120))
    energy_penalty = max(0, min(1, record["energy_consumption"] / 0.25))

    mai = (
        0.24 * comm
        + 0.22 * nav
        + 0.22 * coverage
        + 0.16 * integrity
        + 0.10 * recovery
        - 0.06 * energy_penalty
    )

    return max(0, min(1, mai)), comm, nav, coverage, integrity, recovery


def choose_digital_twin_action(record: Dict) -> Tuple[str, float]:
    """
    Simple digital-twin action projection:
    evaluate candidate actions and choose the one with highest projected MAI.
    """
    base_mai = record["mission_assurance_index"]

    candidates = {
        "continue": base_mai - 0.02,
        "monitor": base_mai + 0.02,
        "reroute": base_mai + 0.07 if record["navigation_score"] < 0.75 else base_mai + 0.01,
        "reassign": base_mai + 0.08 if record["coverage_score"] < 0.75 else base_mai + 0.02,
        "isolate-node": base_mai + 0.09 if record["integrity_score"] < 0.5 else base_mai - 0.02,
        "return-to-base": base_mai + 0.04 if record["mission_assurance_index"] < 0.45 else base_mai - 0.05,
    }

    action = max(candidates, key=candidates.get)
    projected = max(0, min(1, candidates[action]))
    return action, projected


def risk_level(mai: float) -> str:
    if mai >= 0.80:
        return "low"
    if mai >= 0.60:
        return "medium"
    if mai >= 0.40:
        return "high"
    return "critical"


def generate_dataset(config: V3Config) -> pd.DataFrame:
    rows: List[Dict] = []

    for seed in config.seeds:
        random.seed(seed)
        np.random.seed(seed)

        for scenario in SCENARIOS:
            intensity_list = ["none"] if scenario == "normal" else ATTACK_INTENSITIES

            for intensity in intensity_list:
                for run_id, uav_count in enumerate(config.uav_counts, start=1):
                    previous_hash_map = {uav_id: "GENESIS" for uav_id in range(1, uav_count + 1)}

                    for timestamp in range(0, config.simulation_duration, config.telemetry_interval):
                        attack_window = config.attack_start <= timestamp <= config.attack_end

                        for uav_id in range(1, uav_count + 1):
                            record = base_record(
                                seed=seed,
                                timestamp=timestamp,
                                run_id=run_id,
                                uav_id=uav_id,
                                uav_count=uav_count,
                                scenario=scenario,
                                intensity=intensity,
                                config=config,
                                previous_hash=previous_hash_map[uav_id],
                            )

                            affected = (
                                scenario != "normal"
                                and attack_window
                                and np.random.random() < attack_probability(intensity)
                            )

                            if affected:
                                record = apply_attack(record, scenario, intensity, timestamp, uav_id)
                                record["detection_delay_sec"] = int(np.random.uniform(3, 40) / intensity_factor(intensity))
                            else:
                                # false alarms are rare, but possible
                                record["false_alarm_flag"] = 1 if np.random.random() < 0.015 else 0

                            mai, comm, nav, cov, integ, rec = compute_mission_assurance(record)
                            record["mission_assurance_index"] = mai
                            record["communication_score"] = comm
                            record["navigation_score"] = nav
                            record["coverage_score"] = cov
                            record["integrity_score"] = integ
                            record["recovery_score"] = rec
                            record["risk_level"] = risk_level(mai)
                            record["adaptive_action"], record["projected_mission_assurance"] = choose_digital_twin_action(record)

                            record["current_hash"] = hash_record(record, record["previous_hash"])
                            previous_hash_map[uav_id] = record["current_hash"]

                            rows.append(record)

    return pd.DataFrame(rows)


def main() -> None:
    config = V3Config()
    df = generate_dataset(config)

    output_dir = "simulations/datasets"
    os.makedirs(output_dir, exist_ok=True)

    full_path = os.path.join(output_dir, "uav_mission_telemetry_v3_full.csv")
    sample_path = os.path.join(output_dir, "uav_mission_telemetry_v3_sample.csv")
    summary_path = os.path.join(output_dir, "dataset_summary_v3.csv")
    class_path = os.path.join(output_dir, "class_distribution_v3.csv")

    df.to_csv(full_path, index=False)

    sample_size = min(40000, len(df))
    sample_df = df.sample(n=sample_size, random_state=RANDOM_SEED)
    sample_df.to_csv(sample_path, index=False)

    summary = df.groupby(["scenario", "attack_intensity", "actual_attack_type"]).agg(
        records=("actual_attack_type", "count"),
        avg_mai=("mission_assurance_index", "mean"),
        avg_pdr=("packet_delivered", "mean"),
        avg_latency_ms=("latency_ms", "mean"),
        avg_route_deviation=("route_deviation", "mean"),
        avg_coverage=("zone_coverage", "mean"),
        tamper_rate=("tamper_flag", "mean"),
        avg_detection_delay=("detection_delay_sec", "mean"),
    ).reset_index()
    summary.to_csv(summary_path, index=False)

    df["actual_attack_type"].value_counts().to_csv(class_path)

    print(f"Generated full v3 dataset: {full_path}")
    print(f"Generated GitHub-safe v3 sample: {sample_path}")
    print(f"Generated v3 summary: {summary_path}")
    print(f"Generated v3 class distribution: {class_path}")
    print(f"Total full records: {len(df):,}")
    print(f"Sample records: {len(sample_df):,}")
    print("Class distribution:")
    print(df["actual_attack_type"].value_counts())


if __name__ == "__main__":
    main()
