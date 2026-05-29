# RA-MARS Synthetic Dataset Plan

## Purpose
This file defines the synthetic dataset plan for the RA-MARS simulation. The dataset will support AI-based attack detection and mission-assurance evaluation for secure multi-UAV defence surveillance.

## Dataset Goal
Generate structured UAV telemetry and mission-status data under normal and adversarial conditions.

The dataset should help evaluate:

- AI-based attack detection
- Mission-risk scoring
- Adaptive mission continuation
- Tamper-resistant mission logging
- Mission success under attack

## Dataset Type
Synthetic simulation-generated dataset.

This dataset will not be presented as real military UAV data. It will be clearly described as simulation-generated telemetry for controlled evaluation.

## Dataset Scenarios

The dataset should include five classes:

| Class Label | Description |
|---|---|
| normal | No attack |
| jamming | RF jamming affects communication |
| spoofing | GPS/GNSS spoofing affects navigation |
| tampering | Mission data or logs are modified |
| combined | Jamming, spoofing, and tampering occur together |

## Dataset Size Target

Initial target:

| Scenario | Approximate Records |
|---|---:|
| normal | 20,000 |
| jamming | 20,000 |
| spoofing | 20,000 |
| tampering | 20,000 |
| combined | 20,000 |
| Total | 100,000 |

This can be increased later if needed.

## Core Dataset Fields

| Field | Type | Description |
|---|---|---|
| timestamp | integer | Simulation time in seconds |
| run_id | integer | Simulation run identifier |
| uav_id | string | UAV node identifier |
| scenario | string | normal, jamming, spoofing, tampering, or combined |
| x_position | float | UAV x-coordinate |
| y_position | float | UAV y-coordinate |
| expected_x | float | Expected x-coordinate |
| expected_y | float | Expected y-coordinate |
| speed | float | UAV speed |
| battery_level | float | Remaining battery percentage |
| assigned_zone | integer | Assigned mission zone |
| mission_progress | float | Mission-zone completion progress |
| packet_delivered | integer | 1 if packet delivered, 0 otherwise |
| packet_loss_rate | float | Packet loss ratio |
| latency_ms | float | Communication latency |
| route_deviation | float | Distance from expected route |
| gps_jump | float | Sudden abnormal GPS movement |
| velocity_inconsistency | float | Difference between expected and observed velocity |
| log_integrity_status | integer | 1 if valid, 0 if tampered |
| tamper_flag | integer | 1 if record was tampered |
| attack_probability | float | Model-estimated attack probability |
| risk_score | float | Mission-risk score |
| risk_level | string | low, medium, high, or critical |
| adaptive_action | string | continue, monitor, reroute, reassign, or return-to-base |
| label | string | Final class label |

## Normal Scenario Pattern

Expected characteristics:

- Packet delivery ratio: high
- Latency: low
- Route deviation: low
- GPS jump: low
- Velocity inconsistency: low
- Log integrity: valid
- Risk score: low
- Mission progress: steady

## Jamming Scenario Pattern

Expected characteristics:

- Packet delivery ratio decreases
- Packet loss rate increases
- Latency increases
- Telemetry gaps may occur
- Route data may remain valid
- Log integrity may remain valid
- Risk score increases due to communication degradation

## GPS Spoofing Scenario Pattern

Expected characteristics:

- Route deviation increases
- GPS jump increases
- Velocity inconsistency increases
- Packet delivery may remain normal
- Log integrity may remain valid
- Risk score increases due to navigation inconsistency

## Data-Tampering Scenario Pattern

Expected characteristics:

- Log integrity status becomes invalid
- Tamper flag is activated
- Some records show altered position, timestamp, or mission status
- Packet delivery may remain normal
- GPS movement may remain normal
- Risk score increases due to integrity violation

## Combined Attack Pattern

Expected characteristics:

- Packet loss increases
- Latency increases
- Route deviation increases
- GPS jump increases
- Velocity inconsistency increases
- Log integrity may fail
- Risk score becomes high or critical
- Adaptive actions are triggered more often

## Data Splitting Plan

Use the following split:

| Dataset Part | Percentage |
|---|---:|
| Training | 70% |
| Validation | 15% |
| Testing | 15% |

The split should preserve class balance across all attack types.

## Class Balance

Try to keep the five classes balanced at first.

Balanced classes:
- normal: 20%
- jamming: 20%
- spoofing: 20%
- tampering: 20%
- combined: 20%

Later, an imbalanced version may be created to represent realistic attack frequency.

## Data Quality Checks

Before using the dataset, verify:

- No missing required fields
- Class labels are correct
- Risk score stays between 0 and 1
- Battery level stays between 0 and 100
- Latency is non-negative
- Packet loss rate stays between 0 and 1
- Coordinates remain inside or near the mission area
- Tamper flag matches log integrity status
- Combined attacks include multiple abnormal indicators

## Output Dataset Files

Planned output files:

| File | Purpose |
|---|---|
| synthetic_uav_mission_data.csv | Full dataset |
| train_data.csv | Training split |
| validation_data.csv | Validation split |
| test_data.csv | Testing split |
| dataset_summary.csv | Summary statistics |
| class_distribution.csv | Class balance report |

## Manuscript Statement

The manuscript should clearly state:

"The experimental evaluation uses a simulation-generated synthetic UAV telemetry dataset to model normal and adversarial mission conditions. The dataset is not presented as real military flight data. It is used to support controlled evaluation of mission assurance under configurable jamming, GPS spoofing, and data-tampering scenarios."

## Research Integrity Notes

- Do not claim the dataset is real defence data.
- Do not claim real-world military validation.
- Do not manually fabricate final results.
- Use simulation scripts to generate all numerical results.
- Save generated datasets and results in the repository.
