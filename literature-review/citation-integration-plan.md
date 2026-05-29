# RA-MARS Citation Integration Plan

## Purpose

This file maps the verified literature matrix to the final manuscript sections. The goal is to ensure that every major claim in the RA-MARS manuscript is supported by relevant citations.

## Citation Strategy

The manuscript should not randomly list references. Citations should support specific claims in the correct section.

Use the strongest references for each subsection:

---

## 1. Introduction

Use citations supporting:
- Multi-UAV defence surveillance importance
- Contested environments
- RF jamming, GPS/GNSS spoofing, and data tampering
- Mission assurance need

Recommended reference rows:
- 1: Dynamic reconnaissance operations with UAV swarms
- 31: Dynamic UAV swarm collaboration under malicious jamming
- 40: GNSS jamming and spoofing threats in UAV navigation
- 47: UAV swarm network security survey
- 24: DRL resilience enhancement for unmanned weapon system-of-systems

Use these to support the motivation and problem statement.

---

## 2. Related Work: UAV Defence Surveillance and Swarm Reconnaissance

Recommended reference rows:
- 1: Stodola et al. — UAV swarm reconnaissance replanning
- 5: Wang et al. — multi-UAV reconnaissance task reassignment
- 31: Xiang et al. — target tracking under malicious jamming
- 41: Zhao et al. — graph-based MARL for UAV search and tracking
- 42: Zhang et al. — distributed dynamic task allocation
- 44: Liu et al. — MARL-based dynamic task allocation

Purpose:
These references support swarm coordination, reconnaissance, task allocation, target tracking, and mission adaptation.

---

## 3. Related Work: Jamming and Contested Communication

Recommended reference rows:
- 6: MARL-based UAV swarm communication against jamming
- 7: Gradient-monitored RL for jamming detection in FANETs
- 8: Safe MARL against adversarial communications
- 9: Jamming detection at the edge of drone networks
- 10: DRL resource management against jamming
- 31: UAV swarm tracking under malicious jamming
- 32: UAV communication against intelligent jamming
- 33: Cooperative anti-jamming and interference mitigation
- 35: Multi-UAV detection coverage under jamming
- 46: UAV swarm decision-making under incomplete interference information

Purpose:
These references support RF jamming, anti-jamming, spectrum decision-making, contested communication, and adaptive wireless resilience.

---

## 4. Related Work: GPS/GNSS Spoofing and Navigation Trustworthiness

Recommended reference rows:
- 2: Position spoofing attacks on cooperative UAV swarms
- 3: GPS-spoofing attack detection for UAV swarms
- 4: GPS spoofing detection using adversarial ML
- 36: GPS/INS-integrated UAV navigation spoofing
- 37: Resilient multi-sensor UAV navigation
- 38: GNSS-denied UAV navigation survey
- 39: Trusted multisource fusion navigation
- 40: GNSS jamming and spoofing countermeasure survey

Purpose:
These references support navigation spoofing, GPS-denied navigation, sensor fusion, and trusted positioning.

---

## 5. Related Work: UAV Cybersecurity and AI-Based IDS

Recommended reference rows:
- 11: Cybersecurity of UAVs survey
- 12: Security and privacy issues of UAVs
- 13: Cybersecurity attacks and defenses for UAS
- 14: UAS cybersecurity survey
- 26: Cyber-physical IDS for UAVs
- 27: Real-time collaborative IDS in UAV networks
- 28: ML approaches to UAV intrusion detection
- 29: Lightweight IDS for UAVs
- 30: Deep learning anomaly detection in CPS
- 47: UAV swarm security survey

Purpose:
These references support cybersecurity taxonomy, cyber-physical IDS, lightweight AI detection, and UAV swarm security.

---

## 6. Related Work: Blockchain and Tamper-Resistant Logging

Recommended reference rows:
- 16: DASLog secure logging for UAV ecosystems
- 17: Blockchain-based authentication for UAV swarms
- 18: Lightweight blockchain for UAV ad-hoc networks
- 19: Proof-of-stake blockchain for UAV-assisted IoT
- 20: Blockchain-assisted UAV communication survey

Purpose:
These references support tamper-resistant logging, auditability, data provenance, and lightweight blockchain design.

---

## 7. Related Work: Mission Assurance and Resilience

Recommended reference rows:
- 21: Dynamic mission abort policy for swarms
- 22: Resilience evaluation of unmanned autonomous swarm
- 23: UAV swarm resilience considering information exchange capacity
- 24: DRL resilience enhancement for unmanned weapon system-of-systems
- 25: Dynamic resilience evaluation for cross-domain swarms
- 46: Dynamic UAV swarm decision-making under incomplete interference information

Purpose:
These references support mission assurance, resilience, recovery, and adaptive mission continuation.

---

## 8. System Model and Threat Model

Use citations for:
- RF jamming threat model: rows 6, 7, 31, 32, 33
- GPS/GNSS spoofing threat model: rows 2, 3, 36, 39, 40
- UAV cybersecurity threat model: rows 11, 12, 13, 47
- Mission logging threat model: rows 16, 18, 20

---

## 9. Methodology

Use citations carefully:
- AI detection module: rows 26, 27, 29, 30
- Risk and resilience framing: rows 21, 22, 23, 24, 25
- Adaptive mission continuation: rows 5, 41, 42, 44
- Tamper-resistant logging: rows 16, 18, 19, 20

---

## 10. Experimental Setup

Citations are less important here, but use references for:
- synthetic simulation justification
- UAV cybersecurity datasets
- UAV IDS evaluation
- mission-level resilience metrics

Recommended rows:
- 26: Cyber-physical UAV IDS dataset
- 29: UAV-IDS lightweight model
- 21–25: resilience and mission evaluation

---

## 11. Results and Discussion

Use citations only for comparison and interpretation:
- Compare AI detection results with rows 26, 27, 29
- Compare mission resilience framing with rows 21–25
- Compare jamming results with rows 6, 31, 32, 35
- Compare spoofing/navigation findings with rows 36–40
- Compare tamper logging with rows 16, 18, 20

---

## 12. Final Citation Requirements

Before journal submission:

- Add in-text citations to every subsection.
- Verify all DOI values.
- Remove duplicate references.
- Use one citation style consistently.
- Format references according to Defence Technology / Elsevier style.
- Avoid citing too many weak sources.
- Prefer IEEE, Elsevier, ACM, Springer, and Chinese Journal of Aeronautics references.
- Use MDPI only where technically useful and not overrepresented.

## Priority References for Final Manuscript

The highest-value references are:

- Stodola et al., 2025, Scientific Reports
- Bi et al., 2024, IEEE TIFS
- Lv et al., 2023, IEEE TWC
- Lv et al., 2024, IEEE TIFS
- Greco et al., 2021, Applied Soft Computing
- Shao et al., 2024, IEEE TMC
- Mekdad et al., 2023, Computer Networks
- DASLog, 2023, IEEE IoT Journal
- Xiong et al., 2024, Computer Networks
- Sun et al., 2024, Reliability Engineering & System Safety
- Zhang et al., 2024, Reliability Engineering & System Safety
- Hassler et al., 2024, IEEE TITS
- Hadi et al., 2024, IEEE IoT Journal
- Ma et al., 2024, IEEE TVT
- Meng et al., 2025, IEEE/ASME TMECH
- Zeng et al., 2026, IEEE COMST
- Zhao et al., 2025, Chinese Journal of Aeronautics
- Li et al., 2025, Chinese Journal of Aeronautics
- Wang et al., 2024, ACM Computing Surveys

