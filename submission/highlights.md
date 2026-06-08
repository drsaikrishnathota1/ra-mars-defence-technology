# Highlights

- Proposes RA-MARS, a cross-layer mission-assurance digital twin for secure multi-UAV defence surveillance.
- Integrates temporal attack detection, Mission Assurance Index scoring, adaptive continuation, and tamper-resistant provenance.
- Evaluates RF jamming, GPS/GNSS spoofing, mission-data tampering, and combined attack scenarios using synthetic UAV telemetry.
- Achieves 73.61% mission success and a Mission Assurance Index of 0.7012 under stressed attack scenarios.
- Achieves 99.81% macro-F1 for binary attack-versus-normal classification and 99.18% macro-F1 for fine-grained eight-class classification.
- PGD-augmented adversarial training maintains 99.75% macro-F1 under FGSM ε=0.01 and 98.31% macro-F1 under PGD ε=0.05.
- Adds only 11.5 ms framework overhead per telemetry cycle in latency-budget analysis.

- Adds a 1D-CNN temporal baseline achieving 99.96% macro-F1 on binary classification and 98.18% macro-F1 on fine-grained classification.
- Frames results as controlled synthetic-telemetry validation rather than real military flight testing.
