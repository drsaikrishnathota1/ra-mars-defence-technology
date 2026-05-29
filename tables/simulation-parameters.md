# Simulation Parameters

## Target Journal
Defence Technology

## Study Title
RA-MARS: A Resilient AI-Driven Mission Assurance Framework for Secure Multi-UAV Defence Surveillance Under Jamming, GPS Spoofing, and Data-Tampering Attacks

## Simulation Objective
The simulation aims to evaluate how the proposed RA-MARS framework improves mission assurance for multi-UAV defence surveillance under normal and adversarial conditions.

## Simulation Environment

| Parameter | Proposed Value |
|---|---|
| Simulation type | Python-based discrete mission simulation |
| Mission type | Multi-UAV defence surveillance |
| Mission area | 5 km × 5 km surveillance zone |
| Number of UAVs | 10, 20, and 30 UAVs |
| Ground control station | 1 |
| Mission zones | 25 grid-based zones |
| Simulation duration | 600 seconds per run |
| Number of runs | 30 runs per scenario |
| UAV speed | 10–25 m/s |
| UAV communication range | 500–1000 m |
| Telemetry interval | 1 second |
| Initial UAV battery | 100% |
| Energy model | Movement + communication + security overhead |
| Logging interval | Every telemetry cycle |

## Attack Scenarios

| Scenario | Description |
|---|---|
| S1: Normal operation | No attack is applied |
| S2: RF jamming | Packet loss and latency increase in affected UAV links |
| S3: GPS spoofing | False location values are injected into UAV telemetry |
| S4: Data tampering | Mission logs are modified after collection |
| S5: Combined attack | Jamming, GPS spoofing, and data tampering occur together |

## Jamming Attack Parameters

| Parameter | Proposed Value |
|---|---|
| Jamming start time | Random between 100–250 seconds |
| Jamming duration | 60–180 seconds |
| Affected UAVs | 20%–50% of UAV nodes |
| Packet loss under jamming | 20%–60% |
| Additional latency | 50–300 ms |
| Jamming intensity levels | Low, medium, high |

## GPS Spoofing Parameters

| Parameter | Proposed Value |
|---|---|
| Spoofing start time | Random between 150–300 seconds |
| Spoofing duration | 60–180 seconds |
| Affected UAVs | 10%–40% of UAV nodes |
| Location deviation | 20–300 meters |
| Spoofing pattern | gradual drift and sudden jump |
| Detection features | velocity inconsistency, location jump, route deviation |

## Data-Tampering Parameters

| Parameter | Proposed Value |
|---|---|
| Tampering target | telemetry records and mission logs |
| Tampering rate | 5%–30% of records |
| Tampering type | location change, timestamp change, status change |
| Integrity method | hash-chain or blockchain-inspired logging |
| Detection condition | mismatch between stored hash and recalculated hash |

## AI Detection Features

| Feature | Description |
|---|---|
| Packet delivery ratio | Measures communication reliability |
| Average latency | Measures communication delay |
| GPS position change | Detects abnormal location shifts |
| Velocity consistency | Compares speed with expected UAV movement |
| Route deviation | Measures deviation from assigned mission path |
| Battery drain rate | Detects abnormal energy behavior |
| Log integrity status | Indicates whether record hash was altered |
| Mission progress rate | Measures completed zones over time |

## AI Models to Test

| Model | Purpose |
|---|---|
| Random Forest | Main baseline ML classifier |
| Logistic Regression | Simple baseline |
| Support Vector Machine | Classical ML comparison |
| XGBoost or Gradient Boosting | Strong ML classifier |
| Lightweight Neural Network | Optional deep learning comparison |

## Baseline Methods

| Baseline | Description |
|---|---|
| B1: Conventional UAV system | No AI detection, no tamper-resistant logging, no adaptive mission logic |
| B2: AI-only detection | AI detects attacks but does not include tamper-resistant logging or adaptive mission logic |
| B3: Logging-only system | Includes tamper-resistant logs but no AI-based attack detection |
| B4: Non-adaptive secure system | Detects/logs attacks but does not adapt mission decisions |
| B5: Proposed RA-MARS | AI detection + risk scoring + adaptive mission logic + tamper-resistant logging |

## Evaluation Metrics

| Metric | Description |
|---|---|
| Mission success rate | Percentage of mission zones successfully surveyed |
| Attack detection accuracy | Correct classification of attack and normal states |
| Precision | Ratio of true attack detections among predicted attacks |
| Recall | Ratio of detected attacks among actual attacks |
| F1-score | Harmonic mean of precision and recall |
| Packet delivery ratio | Successfully delivered packets divided by total packets |
| Average latency | Mean communication delay |
| Energy consumption | Battery used during mission |
| Tamper-detection rate | Percentage of modified records detected |
| Mission recovery time | Time required to restore stable mission operation |

## Expected Result Direction

RA-MARS is expected to:
- Improve mission success rate under attack
- Increase attack detection accuracy
- Improve tamper-detection performance
- Maintain acceptable latency overhead
- Reduce mission degradation during combined attacks
- Provide better operational resilience compared with baseline methods

## Notes
The simulation should avoid unrealistic claims. Results should be presented as simulation-based evidence, not real-world military deployment validation.
