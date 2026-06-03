"""
PX4/Gazebo-style telemetry generator for RA-MARS validation.

This is a software-only MAVLink/PX4-style telemetry emulator.
It does not claim real PX4/Gazebo execution.
It creates simulator-style UAV mission telemetry with safe software-emulated:
- packet-loss / jamming effects
- GPS drift / spoofing effects
- mission-log tampering effects
"""

from pathlib import Path
import hashlib
import numpy as np
import pandas as pd


OUT_DIR = Path("validation/px4_gazebo/data")
OUT_DIR.mkdir(parents=True, exist_ok=True)

RNG = np.random.default_rng(42)

UAV_COUNT = 3
DURATION_SEC = 600
TELEMETRY_HZ = 1
ROWS_PER_UAV = DURATION_SEC * TELEMETRY_HZ

BASE_LAT = 38.6270
BASE_LON = -90.1994


def hash_record(row_dict, previous_hash):
    payload = "|".join(str(row_dict[k]) for k in sorted(row_dict.keys()))
    payload = previous_hash + "|" + payload
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def attack_type_for_time(t):
    if 150 <= t < 260:
        return "jamming"
    if 260 <= t < 380:
        return "spoofing"
    if 380 <= t < 460:
        return "tampering"
    if 460 <= t < 540:
        return "combined"
    return "normal"


def make_uav_path(uav_id, t):
    # Simple waypoint-style lawnmower trajectory.
    phase = (t / DURATION_SEC) * 2 * np.pi
    offset = 120 * (uav_id - 1)

    local_x = 600 * np.sin(phase) + offset
    local_y = 400 * np.cos(phase * 0.8) + 80 * uav_id
    local_z = 80 + 5 * np.sin(phase * 1.2)

    vx = 600 * np.cos(phase) * (2 * np.pi / DURATION_SEC)
    vy = -400 * 0.8 * np.sin(phase * 0.8) * (2 * np.pi / DURATION_SEC)
    vz = 5 * 1.2 * np.cos(phase * 1.2) * (2 * np.pi / DURATION_SEC)

    return local_x, local_y, local_z, vx, vy, vz


def main():
    records = []
    previous_hash_by_uav = {uav_id: "GENESIS" for uav_id in range(1, UAV_COUNT + 1)}

    for uav_id in range(1, UAV_COUNT + 1):
        for t in range(ROWS_PER_UAV):
            attack = attack_type_for_time(t)

            local_x, local_y, local_z, vx, vy, vz = make_uav_path(uav_id, t)

            packet_received = 1
            latency_ms = RNG.normal(45, 8)
            gps_drift_m = RNG.normal(0, 0.8)
            route_deviation_m = abs(RNG.normal(4, 1.5))
            tamper_flag = 0

            if attack in ["jamming", "combined"] and uav_id in [1, 2]:
                packet_received = int(RNG.random() > 0.32)
                latency_ms += RNG.normal(90, 25)

            if attack in ["spoofing", "combined"] and uav_id in [2, 3]:
                drift = min((t - 260) * 0.35, 45) if t >= 260 else 0
                jump = 20 if t in [300, 301, 302, 470, 471] else 0
                gps_drift_m = abs(drift + jump + RNG.normal(0, 2.0))
                route_deviation_m += gps_drift_m * 0.7
                local_x += gps_drift_m

            if attack in ["tampering", "combined"] and uav_id == 3:
                tamper_flag = int(RNG.random() < 0.25)

            battery = max(15, 100 - 0.08 * t - RNG.normal(0, 0.2))
            mission_progress = min(100, (t / DURATION_SEC) * 100 + RNG.normal(0, 0.5))
            waypoint_id = int((mission_progress // 10) + 1)
            mission_mode = "AUTO.MISSION"

            lat = BASE_LAT + local_y / 111_111
            lon = BASE_LON + local_x / (111_111 * np.cos(np.deg2rad(BASE_LAT)))

            row = {
                "timestamp": t,
                "uav_id": uav_id,
                "lat": round(lat, 8),
                "lon": round(lon, 8),
                "alt": round(local_z, 3),
                "local_x": round(local_x, 3),
                "local_y": round(local_y, 3),
                "local_z": round(local_z, 3),
                "vx": round(vx, 4),
                "vy": round(vy, 4),
                "vz": round(vz, 4),
                "battery": round(battery, 3),
                "mission_mode": mission_mode,
                "waypoint_id": waypoint_id,
                "mission_progress": round(mission_progress, 3),
                "packet_received": packet_received,
                "latency_ms": round(max(1, latency_ms), 3),
                "gps_drift_m": round(abs(gps_drift_m), 3),
                "route_deviation_m": round(route_deviation_m, 3),
                "tamper_flag": tamper_flag,
                "attack_type": attack,
            }

            current_hash = hash_record(row, previous_hash_by_uav[uav_id])
            row["previous_hash"] = previous_hash_by_uav[uav_id]
            row["record_hash"] = current_hash
            previous_hash_by_uav[uav_id] = current_hash

            records.append(row)

    df = pd.DataFrame(records)

    # Create a tampered copy to test hash-chain verification.
    tampered = df.copy()
    tamper_indices = tampered.index[tampered["tamper_flag"] == 1].tolist()
    for idx in tamper_indices:
        tampered.loc[idx, "local_x"] = tampered.loc[idx, "local_x"] + RNG.normal(30, 8)

    raw_path = OUT_DIR / "px4_style_mavlink_telemetry.csv"
    tampered_path = OUT_DIR / "px4_style_mavlink_telemetry_tampered.csv"

    df.to_csv(raw_path, index=False)
    tampered.to_csv(tampered_path, index=False)

    print(f"Saved raw PX4-style telemetry: {raw_path}")
    print(f"Saved tampered telemetry: {tampered_path}")
    print(f"Rows: {len(df)}")
    print("Attack distribution:")
    print(df["attack_type"].value_counts())


if __name__ == "__main__":
    main()
