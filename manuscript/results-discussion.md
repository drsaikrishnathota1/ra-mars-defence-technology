# Results and Discussion

## Overview

This section presents the v2 simulation results for the RA-MARS framework. The evaluation uses a simulation-generated synthetic multi-UAV telemetry dataset with row-level attack labels and non-leakage telemetry features. The results are intended to provide controlled simulation-based evidence of mission assurance under normal operation, RF jamming, GPS/GNSS spoofing, mission-data tampering, and combined attack scenarios.

RA-MARS is compared against four baseline systems:

- Conventional UAV System
- AI-Only Detection System
- Logging-Only System
- Non-Adaptive Secure System
- Proposed RA-MARS Framework

The evaluation includes both AI attack-detection performance and mission-level resilience metrics.

## AI Attack Detection Performance

The v2 attack-detection experiment uses balanced sampling across the row-level attack classes. Only non-leakage telemetry features are used for training:

- packet loss rate
- latency
- route deviation
- GPS jump
- velocity inconsistency
- battery level
- mission progress

The best-performing model is **Gradient Boosting**, achieving:

| Metric | Value |
|---|---:|
| Accuracy | 0.8987 |
| Macro Precision | 0.9050 |
| Macro Recall | 0.8986 |
| Macro F1-score | 0.8971 |

These results are more realistic than the earlier clean-label experiment because the model does not use direct leakage features such as risk score, tamper flag, or log-integrity status. The results show that AI-based detection can classify cyber-physical mission states with strong but not artificially perfect performance.

Related figure:

- `figures/graphs/final/graph1_ai_detection_performance_v2.png`

## Mission Success Rate

Mission success rate is the most important mission-assurance metric in this study. Under the combined attack scenario, the Conventional UAV System achieves a mission success rate of **63.21%**, while RA-MARS achieves **78.60%**.

Under the jamming scenario, the Conventional UAV System achieves **66.92%**, while RA-MARS achieves **83.22%**.

These results indicate that RA-MARS improves mission continuity under adversarial conditions by combining AI-based attack detection, mission-risk scoring, adaptive mission-continuation logic, and tamper-resistant logging.

Related figure:

- `figures/graphs/final/graph2_mission_success_rate_v2.png`

## Communication Performance

Communication performance is evaluated using packet delivery ratio and average latency. Under the combined attack scenario, the packet delivery ratio improves from **0.761** for the Conventional UAV System to **0.885** for RA-MARS.

This improvement suggests that adaptive mission logic and risk-aware operation can help reduce the mission-level impact of communication degradation under jamming and combined attacks.

Related figures:

- `figures/graphs/final/graph3_packet_delivery_ratio_v2.png`
- `figures/graphs/final/graph4_average_latency_v2.png`

## Navigation Reliability

Navigation reliability is evaluated using average route deviation. Under the combined attack scenario, the Conventional UAV System produces an average route deviation of **67.32 m**, while RA-MARS reduces this to **48.00 m**.

This reduction supports the role of mission-risk scoring and adaptive mission response in limiting the operational effect of GPS/GNSS spoofing and route deviation.

Related figure:

- `figures/graphs/final/graph5_route_deviation_v2.png`

## Tamper-Detection Performance

The tamper-resistant logging component is evaluated using tamper-detection rate. RA-MARS achieves a tamper-detection rate of **0.96** in the tampering scenario and **0.96** in the combined attack scenario.

These results support the use of lightweight hash-chain or blockchain-inspired logging as a mission-data trustworthiness layer. The logging module should not be interpreted as the primary novelty of RA-MARS, but as a supporting component for preserving mission-record integrity.

Related figure:

- `figures/graphs/final/graph6_tamper_detection_rate_v2.png`

## Energy Consumption and Operational Overhead

RA-MARS introduces additional operational overhead because it includes AI detection, mission-risk scoring, adaptive decision logic, and tamper-resistant logging. Under the combined attack scenario, estimated energy consumption increases from **6.80%** for the Conventional UAV System to **8.28%** for RA-MARS.

This overhead is expected because RA-MARS performs additional monitoring and response functions. However, the overhead is justified in the simulation because RA-MARS improves mission success, packet delivery, route stability, tamper detection, and recovery time.

Related figure:

- `figures/graphs/final/graph7_energy_consumption_v2.png`

## Mission Recovery Time

Mission recovery time evaluates how quickly each system restores stable mission operation after attack detection. Under the combined attack scenario, the Conventional UAV System has an estimated recovery time of **117.64 s**, while RA-MARS reduces this to **67.97 s**.

This result supports the mission-assurance value of adaptive mission-continuation logic. Detection alone is not sufficient; mission recovery requires linking detection results to risk-aware operational decisions.

Related figure:

- `figures/graphs/final/graph8_mission_recovery_time_v2.png`

## Discussion

The v2 results show that RA-MARS improves mission assurance across multiple operational dimensions. The framework improves mission success rate, communication reliability, navigation stability, tamper detection, and recovery time compared with the selected baselines.

The most important finding is that RA-MARS evaluates UAV resilience at the mission level rather than only at the attack-classification level. This is important for defence UAV surveillance because operational success depends not only on detecting an attack, but also on maintaining surveillance coverage, communication continuity, navigation trustworthiness, and reliable mission records.

The results also show a realistic tradeoff. RA-MARS improves resilience but introduces additional energy and operational overhead. This tradeoff should be acknowledged clearly because secure and resilient UAV systems typically require additional computation, communication, and logging operations.

## Research Integrity Note

The results are based on simulation-generated synthetic UAV telemetry data. They should not be interpreted as real-world military flight validation. The results provide controlled simulation-based evidence that integrated mission assurance can improve multi-UAV surveillance resilience under jamming, spoofing, tampering, and combined attacks.

Further validation using hardware-in-the-loop testing, real UAV experiments, realistic RF environments, and operational datasets is required before any real-world deployment claims can be made.

## Summary

The v2 evaluation supports the core claim of RA-MARS: integrating AI-based attack detection, mission-risk scoring, adaptive mission-continuation logic, and tamper-resistant logging can improve secure multi-UAV defence surveillance under contested conditions. The strongest evidence is the improvement in mission success and recovery time under combined attacks, together with strong but realistic AI detection performance.
