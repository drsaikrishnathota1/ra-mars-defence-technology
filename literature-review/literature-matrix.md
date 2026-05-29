# RA-MARS Literature Matrix

## Purpose
This file tracks all papers reviewed for the RA-MARS manuscript.

## Target
- Total references: 45–70
- Recent references from 2021–2026: at least 25

## Literature Matrix

| No. | Citation | Year | Venue | Category | Problem Addressed | Method Used | Dataset / Simulation | Metrics | Strength | Limitation | Relevance to RA-MARS | Gap Supported |
|---:|---|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | Stodola, P., Nohel, J., & Horák, L., “Dynamic reconnaissance operations with UAV swarms: adapting to environmental changes,” Scientific Reports, 2025. | 2025 | Scientific Reports | UAV swarm reconnaissance | Static mission models cannot adapt to real-time mission changes or UAV availability loss. | Ant Colony Optimisation with Pheromone Matrix Initialisation for dynamic replanning. | Simulation; Czech MoD LANDOPS-related scenarios. | Coverage rate; convergence speed; replanning quality. | Defence-relevant UAV swarm reconnaissance; supports dynamic adaptation. | Simulation only; does not directly address EW, GPS spoofing, or tamper-resistant logging. | Supports RA-MARS adaptive mission replanning under degraded swarm conditions. | G1, G2 |
| 2 | Bi, S., Li, K., Hu, S., Ni, W., Wang, C., & Wang, X., “Detection and Mitigation of Position Spoofing Attacks on Cooperative UAV Swarm Formations,” IEEE Transactions on Information Forensics and Security, 2024. | 2024 | IEEE Transactions on Information Forensics and Security | GPS/position spoofing UAV swarm | Coordinated spoofing in UAV swarms can defeat traditional pairwise detection methods. | Localization feasibility formulation using semidefinite relaxation and malicious UAV identification algorithms. | Simulation; distributed, collusion, and mixed attack scenarios. | Detection success rate; false positive rate; false negative rate. | Strong mathematical treatment and direct UAV swarm spoofing relevance. | Computational complexity may increase for large swarms; no real-world flight validation. | Supports RA-MARS navigation integrity and spoofing-detection justification. | G1, G3 |
| 3 | Mykytyn, P., Brzozowski, M., Dyka, Z., & Langendoerfer, P., “GPS-Spoofing Attack Detection Mechanism for UAV Swarms,” 2023 IEEE Mediterranean Conference on Embedded Computing, 2023. | 2023 | IEEE MECO | GPS spoofing UAV swarm | Civil GPS signals are unauthenticated and vulnerable to spoofing in UAV swarms. | Cross-validation of GPS-coordinate distances with IR-UWB ranging distances. | Simulation; single-transmitter and multi-transmitter spoofing scenarios. | Detection accuracy; computational overhead; energy overhead. | Lightweight swarm-oriented spoofing detection without major UAV modification. | Relies on reliable UWB ranging; limited field validation. | Supports RA-MARS spoofing-detection motivation and navigation-trustworthiness gap. | G1, G3 |
| 4 | Alhoraibi, L., Alghazzawi, D., & Alhebshi, R., “Detection of GPS Spoofing Attacks in UAVs Based on Adversarial Machine Learning Model,” Sensors, vol. 24, no. 18, article 6156, 2024. | 2024 | Sensors | AI-based GPS spoofing detection | Existing UAV GPS spoofing detectors may be vulnerable to adversarial evasion. | Adversarial machine learning model with adversarial data augmentation. | UCI UAV Intrusion Detection dataset; GPS spoofing attack classes. | Detection accuracy; robustness; false positive rate; false negative rate. | Addresses adversarial robustness in ML-based GPS spoofing detection. | Dataset-based evaluation; real contested-environment performance remains unverified. | Supports RA-MARS need for robust AI-based spoofing detection. | G1, G3 |
| 5 | Wang, G., Lv, X., & Yan, X., “A Two-Stage Distributed Task Assignment Algorithm Based on Contract Net Protocol for Multi-UAV Cooperative Reconnaissance Task Reassignment in Dynamic Environments,” Sensors, vol. 23, no. 18, article 7980, 2023. | 2023 | Sensors | Multi-UAV reconnaissance task reassignment | Dynamic events can cause mission failure, and centralized reassignment can create communication bottlenecks. | Two-stage distributed task assignment algorithm based on Contract Net Protocol. | Simulation; dynamic cooperative reconnaissance reassignment scenarios. | Task completion rate; communication burden; combat efficiency. | Distributed design; handles UAV heterogeneity, dynamic events, and time constraints. | Does not address adversarial jamming, spoofing, or data tampering. | Supports RA-MARS distributed/adaptive mission management under degraded conditions. | G1, G2 |

## Category Codes

1. UAV defence surveillance  
2. Multi-UAV mission planning  
3. Mission assurance  
4. RF jamming detection  
5. Anti-jamming communication  
6. GPS/GNSS spoofing detection  
7. AI anomaly detection  
8. UAV cybersecurity  
9. Secure UAV communication  
10. Blockchain/tamper-resistant logging  
11. Resilient autonomous systems  
12. Contested environments  

## Gap Mapping

| Gap Code | Gap Description |
|---|---|
| G1 | Existing work focuses on isolated UAV threats rather than combined jamming, spoofing, and tampering. |
| G2 | Existing work emphasizes attack detection but not mission continuity. |
| G3 | Existing AI detection work is not linked to mission-risk scoring. |
| G4 | Existing UAV security work underemphasizes trustworthy mission logging. |
| G5 | Existing frameworks lack comparative evaluation using mission-level metrics. |
| G6 | Existing work has limited defence-oriented mission-assurance framing. |

## Notes
Every paper should be checked for real title, authors, venue, year, DOI, or publisher link before final submission.
