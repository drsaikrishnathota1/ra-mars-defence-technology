# RA-MARS Novelty Gap

## Target Journal
Defence Technology

## Working Title
RA-MARS: A Resilient AI-Driven Mission Assurance Framework for Secure Multi-UAV Defence Surveillance Under Jamming, GPS Spoofing, and Data-Tampering Attacks

## Background
Multi-UAV systems are increasingly used for defence surveillance, reconnaissance, border monitoring, critical-infrastructure protection, and battlefield situational awareness. However, these systems are vulnerable in contested environments where adversaries may disrupt communications, manipulate navigation signals, and compromise mission records.

Existing studies have investigated UAV surveillance, AI-based anomaly detection, RF jamming detection, GPS spoofing detection, secure UAV communication, and blockchain-based data integrity. However, many studies address these issues separately rather than as an integrated mission-assurance problem.

## Core Research Gap
Most existing UAV security studies focus on one isolated problem, such as detecting jamming, identifying GPS spoofing, securing communication, or preserving data integrity. However, defence UAV missions often face multiple simultaneous threats that affect communication reliability, navigation trustworthiness, mission continuity, and data integrity at the same time.

There is a need for an integrated mission-assurance framework that can jointly detect cyber-electromagnetic threats, estimate mission risk, support adaptive mission continuation, and preserve tamper-resistant mission records for multi-UAV defence surveillance.

## Specific Gaps Identified

### Gap 1: Limited Integration of Multiple Threats
Many UAV security studies focus only on a single threat, such as jamming or GPS spoofing. Defence missions require protection against combined attack scenarios involving communication disruption, navigation manipulation, and mission-data tampering.

### Gap 2: Lack of Mission-Assurance Perspective
Prior work often focuses on attack detection accuracy alone. However, in defence surveillance, the more important question is whether the UAV mission can continue successfully under degraded or adversarial conditions.

### Gap 3: Weak Link Between Attack Detection and Mission Decision-Making
Many AI-based anomaly detection methods identify abnormal behavior but do not connect detection outputs to mission-risk scoring or adaptive mission-continuation decisions.

### Gap 4: Insufficient Focus on Mission-Data Trustworthiness
UAV mission logs, telemetry records, and surveillance outputs must remain trustworthy for post-mission analysis and command accountability. Existing studies often underemphasize tamper-resistant mission logging as part of mission assurance.

### Gap 5: Limited Comparative Evaluation
Many conceptual frameworks do not compare against multiple baselines using operational metrics such as mission success rate, packet delivery ratio, latency, energy consumption, attack detection accuracy, and tamper-detection rate.

## Proposed Novelty of RA-MARS
RA-MARS addresses these gaps by proposing an integrated defence-oriented mission assurance framework for multi-UAV surveillance in contested environments. The framework combines AI-based attack detection, mission-risk scoring, adaptive mission-continuation logic, and blockchain-inspired tamper-resistant logging.

Instead of treating UAV cybersecurity, communication reliability, navigation trustworthiness, and mission-record integrity as separate issues, RA-MARS connects them into a unified mission-assurance workflow.

## Main Novel Contributions

1. RA-MARS provides an integrated framework for multi-UAV defence surveillance under RF jamming, GPS spoofing, and mission-data tampering attacks.

2. The framework introduces a mission-risk scoring mechanism that links AI-based attack detection outputs with mission-continuation decisions.

3. RA-MARS incorporates tamper-resistant mission logging to improve the integrity, traceability, and auditability of UAV surveillance records.

4. The study evaluates the framework using multiple operational metrics, including mission success rate, attack detection accuracy, packet delivery ratio, latency, energy consumption, tamper-detection rate, and mission recovery time.

5. The proposed framework is compared against conventional UAV surveillance, AI-only attack detection, blockchain-only logging, and non-adaptive mission baselines.

## Novelty Statement for Manuscript
Unlike prior studies that focus on isolated UAV security functions, RA-MARS presents an integrated mission-assurance framework for defence-oriented multi-UAV surveillance. The proposed framework jointly addresses communication disruption, navigation manipulation, and mission-data tampering by combining AI-based attack detection, mission-risk scoring, adaptive mission-continuation logic, and tamper-resistant logging. This integrated approach enables the evaluation of UAV resilience not only by attack detection accuracy but also by mission success, communication reliability, operational overhead, and data trustworthiness under contested conditions.

## Important Positioning
RA-MARS should not be presented as a generic AI or blockchain framework. It should be positioned as a defence mission-assurance framework for multi-UAV surveillance in contested environments.

## What to Avoid
- Do not make quantum the main claim.
- Do not overclaim real-world deployment.
- Do not claim military-grade validation without actual field testing.
- Do not present blockchain as the main novelty.
- Do not write the paper as only a conceptual framework.
- Do not submit with fewer than 45 references.
- Do not ignore recent literature from 2021–2026.

