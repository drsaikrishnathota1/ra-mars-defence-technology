Dr. Sai Krishna Thota
Email: drsaikrishnathota1@gmail.com
GitHub: github.com/drsaikrishnathota1/ra-mars-defence-technology

Editor-in-Chief
Defence Technology
KeAi Communications / Elsevier

Dear Editor,

I am submitting the manuscript **"RA-MARS: An AI-Driven Cross-Layer Mission Assurance Digital Twin for Secure Multi-UAV Defence Surveillance Under Cyber-Electromagnetic and Navigation Attacks"** for consideration for publication in *Defence Technology*.

## Why this paper suits Defence Technology

Multi-UAV defence surveillance systems face growing cyber-electromagnetic threats including RF jamming, GPS/GNSS spoofing, and mission-data tampering. Existing studies address these threats in isolation. This paper proposes RA-MARS, a mission-level assurance framework that connects temporal AI-based attack detection, Mission Assurance Index scoring, digital twin action selection, adaptive mission continuation, and SHA-256 hash-chain tamper-resistant logging into a unified cross-layer framework.

## Key contributions and results

The v4 simulation evaluation, conducted using physics-based RF channel modelling (Friis free-space path loss, SINR-based packet delivery ratio), produced the following results:

- **Binary attack detection:** 95.73% macro F1-score (Binary LSTM) — operationally meaningful for the attack/no-attack decision
- **Mission success rate:** 73.61 ± 0.87% under stressed combined attack scenarios
- **Mission Assurance Index:** 0.7012 ± 0.0042 under full RA-MARS
- **RF physics validation:** Normal SINR 39.9 dB; high-intensity jammed SINR 26.9 dB; Friis-derived PDR degradation from 1.000 to 0.736
- **Framework overhead:** 11.5 ms per telemetry cycle (1.15% of the 1-second MAVLink interval)
- **Adversarial robustness:** Binary LSTM F1 degrades to 0.307 under FGSM at ε=0.01, motivating adversarial training as future work
- **Tamper detection:** 100% under the defined Dolev-Yao bounded attacker model
- **PX4-style telemetry emulation:** 1,800 MAVLink-style telemetry records from three UAVs demonstrate simulator-style RA-MARS processing without claiming real PX4/Gazebo SITL, hardware-in-the-loop, or flight-test validation

The simulation code, synthetic dataset generation scripts, evaluation scripts, and all result files are available at: https://github.com/drsaikrishnathota1/ra-mars-defence-technology

## Scope confirmation

This manuscript has not been published previously, is not under consideration elsewhere, and all co-authors have approved the submission. The study uses synthetic simulation data only; no real military UAV data, human subjects, or animals were involved.

Yours sincerely,

Dr. Sai Krishna Thota
