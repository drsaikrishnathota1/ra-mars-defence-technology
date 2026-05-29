# RA-MARS Full Manuscript Draft

## Working Title

RA-MARS: A Resilient AI-Driven Mission Assurance Framework for Secure Multi-UAV Defence Surveillance Under Jamming, GPS/GNSS Spoofing, and Data-Tampering Attacks

## Target Journal

Defence Technology

---

# Abstract

Multi-UAV surveillance systems are increasingly used in defence reconnaissance, border monitoring, battlefield awareness, and critical-infrastructure protection. However, their operational reliability can be degraded in contested environments where adversaries conduct radio-frequency jamming, GPS/GNSS spoofing, and mission-data tampering. These attacks can reduce communication reliability, corrupt navigation decisions, compromise mission records, and weaken operational trust during time-sensitive defence missions.

To address these challenges, this paper proposes RA-MARS, a resilient AI-driven mission assurance framework for secure multi-UAV defence surveillance. RA-MARS integrates AI-based attack detection, mission-risk scoring, adaptive mission-continuation logic, and blockchain-inspired tamper-resistant mission logging. The framework is designed to detect communication, navigation, and data-integrity anomalies while supporting mission continuity under adversarial conditions.

A simulation-based evaluation is conducted using synthetic multi-UAV telemetry data under normal, jamming, GPS/GNSS spoofing, data-tampering, and combined attack scenarios. The proposed framework is compared with conventional UAV surveillance, AI-only detection, logging-only, and non-adaptive secure baselines. Using balanced row-level attack labels and non-leakage telemetry features, the best-performing model achieved 89.87% accuracy, 90.50% macro precision, 89.86% macro recall, and 89.71% macro F1-score. Under the combined attack scenario, RA-MARS improved mission success rate from 63.21% to 78.60%, increased packet delivery ratio from 0.761 to 0.885, reduced average route deviation from 67.32 m to 48.00 m, and reduced mission recovery time from 117.64 s to 67.97 s compared with the conventional UAV baseline.

The results indicate that RA-MARS improves UAV resilience not only through attack detection but also through mission continuity, communication reliability, navigation stability, operational recovery, and mission-data trustworthiness. The study provides simulation-based evidence for an integrated defence-oriented mission assurance model for secure multi-UAV surveillance in contested environments.

---

# Introduction

Multi-UAV surveillance systems have become increasingly important in modern defence operations because they provide distributed sensing, rapid situational awareness, flexible reconnaissance, and scalable monitoring of hostile or remote environments. Compared with single-UAV platforms, coordinated UAV teams can cover larger mission areas, improve redundancy, and support time-sensitive decision-making in border surveillance, battlefield reconnaissance, convoy protection, and critical-infrastructure monitoring.

However, the operational benefits of multi-UAV systems also introduce new mission-assurance challenges. In contested environments, adversaries may deliberately disrupt UAV communication, manipulate navigation signals, or tamper with mission records to degrade surveillance reliability and reduce operational trust. These attacks are especially concerning in defence missions where communication continuity, navigation accuracy, and trustworthy mission records are essential for command decisions and post-mission analysis.

Radio-frequency jamming, GPS spoofing, and mission-data tampering represent three major threats to defence UAV operations. Jamming can increase packet loss, delay command-and-control communication, and isolate UAV nodes from the ground control station. GPS spoofing can mislead UAV navigation by injecting false position information, causing incorrect routing, loss of formation, or mission deviation. Data tampering can compromise the integrity of telemetry records, surveillance logs, and mission evidence, reducing the reliability of operational assessment and command accountability.

Existing UAV security studies often focus on isolated problems such as jamming detection, GPS spoofing identification, secure communication, or data-integrity protection. Although these studies provide valuable insights, defence UAV missions frequently face combined and cascading threats. For example, a UAV swarm may experience communication degradation from jamming while also receiving manipulated navigation data and producing mission logs that are vulnerable to tampering. In such conditions, attack detection alone is not sufficient. A defence-oriented UAV system must also estimate mission risk, support adaptive continuation, and preserve trustworthy mission records.

To address this need, this paper proposes RA-MARS, a resilient AI-driven mission assurance framework for secure multi-UAV defence surveillance under jamming, GPS spoofing, and data-tampering attacks. RA-MARS integrates AI-based attack detection, mission-risk scoring, adaptive mission-continuation logic, and blockchain-inspired tamper-resistant mission logging. Instead of treating UAV cybersecurity, mission continuity, and data integrity as separate problems, RA-MARS connects them into a unified mission-assurance workflow.

The main contributions of this paper are as follows:

1. A resilient AI-driven mission assurance framework is proposed for multi-UAV defence surveillance in contested environments affected by RF jamming, GPS spoofing, and mission-data tampering.

2. An AI-based attack detection mechanism is developed to identify abnormal communication, navigation, and mission-record patterns during UAV surveillance operations.

3. A mission-risk scoring model is introduced to estimate operational degradation and support adaptive mission-continuation decisions under adversarial conditions.

4. A blockchain-inspired tamper-resistant logging mechanism is incorporated to improve the integrity, traceability, and auditability of UAV mission records.

5. A simulation-based evaluation plan is established to compare the proposed framework with conventional UAV surveillance, AI-only detection, blockchain-only logging, and non-adaptive security baselines using mission success rate, detection accuracy, packet delivery ratio, latency, energy consumption, and tamper-detection performance.

The remainder of this paper is organized as follows. Section 2 reviews related work on UAV defence surveillance, AI-based attack detection, jamming and spoofing mitigation, UAV cybersecurity, and tamper-resistant mission logging. Section 3 presents the system model and threat model. Section 4 describes the proposed RA-MARS framework. Section 5 explains the experimental setup and evaluation metrics. Section 6 discusses the results and comparative analysis. Section 7 presents limitations and future work. Section 8 concludes the paper.

---

# Related Work

## Overview

This section reviews prior work related to UAV defence surveillance, contested UAV communication, GPS/GNSS spoofing, UAV cybersecurity, AI-based intrusion detection, tamper-resistant mission logging, and mission assurance. The purpose of this section is to identify the research gap that motivates RA-MARS.

## UAV Defence Surveillance and Swarm Reconnaissance

Multi-UAV systems are increasingly studied for reconnaissance, surveillance, target tracking, and dynamic mission coverage [1,5,30,39–41]. Compared with single-UAV platforms, UAV swarms can improve coverage, redundancy, and operational flexibility. Recent studies have investigated dynamic reconnaissance planning, multi-target tracking, cooperative task allocation, and swarm-level replanning under UAV loss or mission changes.

However, many reconnaissance and task-allocation studies assume that communication and navigation channels remain sufficiently reliable. This assumption is difficult to maintain in contested environments where RF jamming, GPS spoofing, and cyber-physical attacks may degrade swarm coordination. Therefore, defence-oriented UAV surveillance requires not only coverage optimization but also mission assurance under adversarial disruption.

## Jamming, Anti-Jamming, and Contested UAV Communication

RF jamming is one of the most critical threats to UAV swarm operations because it can reduce packet delivery ratio, increase communication latency, and disrupt command-and-control links [6–10,30–33,42]. Existing studies have proposed reinforcement learning, game-theoretic optimization, federated reinforcement learning, cooperative anti-jamming mechanisms, and jamming-aware UAV swarm collaboration for UAV communications under adversarial interference.

These works provide important communication-level resilience mechanisms. However, most of them focus on communication performance metrics such as throughput, bit error rate, signal-to-interference-plus-noise ratio, latency, and power consumption. Fewer studies connect jamming detection and anti-jamming control to mission-level outcomes such as surveillance coverage, mission success rate, mission recovery time, and trustworthy mission records.

## GPS/GNSS Spoofing and Navigation Trustworthiness

GPS/GNSS spoofing can mislead UAV navigation by injecting false position information or gradually deviating UAV routes while avoiding simple detection [2–4,34–38]. Recent studies have examined GPS spoofing detection in UAV swarms, GPS/INS spoofing attacks, GNSS-denied navigation, and trusted multisource fusion for UAV positioning under interference and spoofing attacks.

These studies show that UAV navigation trustworthiness cannot depend only on GNSS measurements. Alternative navigation sources, sensor fusion, inertial navigation, visual odometry, and integrity monitoring are important for maintaining positioning reliability. However, spoofing detection is often studied separately from mission-risk assessment and adaptive mission continuation. In defence surveillance, navigation anomalies should be linked to route deviation, mission-zone coverage, and operational decision-making.

## UAV Cybersecurity and AI-Based Intrusion Detection

UAV cybersecurity research has examined attacks affecting communication, software, payloads, sensors, network traffic, and cyber-physical behavior [11–14,25–29,43]. Recent surveys provide taxonomies of UAV threats and countermeasures, while AI-based intrusion detection studies use cyber-physical feature fusion, collaborative deep learning, lightweight neural networks, and anomaly detection methods to identify attacks.

AI-based intrusion detection can improve UAV attack awareness, especially when telemetry and network features are combined. However, detection accuracy alone is not enough for mission assurance. A UAV system may correctly detect an attack but still fail the mission if detection is not connected to risk scoring, adaptive response, and mission recovery. This motivates a framework that uses AI detection as one part of a broader mission-assurance workflow.

## Blockchain and Tamper-Resistant UAV Mission Logging

Blockchain, hash-chain, Merkle-tree, and lightweight consensus mechanisms have been proposed to improve UAV data integrity, authentication, secure communication, and auditability [15–19]. Secure logging frameworks such as DASLog show how UAV ecosystem records can be verified using cryptographic proofs and decentralized audit structures. Lightweight blockchain mechanisms also address the resource limitations of UAV ad-hoc networks.

However, blockchain should not be treated as the main novelty of RA-MARS. Instead, tamper-resistant logging is used as a supporting component to preserve mission-data trustworthiness. Existing blockchain-UAV studies often focus on data integrity or authentication but do not fully connect log integrity with mission assurance under jamming, spoofing, and operational degradation.

## Mission Assurance, Resilience, and Adaptive Swarm Coordination

Mission assurance and resilience research examines how autonomous swarms maintain acceptable performance under failure, degradation, uncertainty, or adversarial interference [20–24,42]. Recent studies have proposed dynamic mission abort policies, resilience evaluation metrics, multistate network models, unmanned weapon system-of-systems recovery strategies, dynamic resilience evaluation under confrontation, and distributed task allocation for UAV swarms.

These studies are important because they shift the focus from isolated attack prevention to operational continuity and recovery. However, many resilience models treat degradation abstractly and do not explicitly integrate cyber-electromagnetic threats such as jamming, spoofing, and mission-data tampering. RA-MARS addresses this gap by connecting cyber-physical attack detection, mission-risk scoring, adaptive mission continuation, and tamper-resistant logging in one framework.

## Research Gap

The reviewed literature shows that UAV surveillance, anti-jamming communication, GPS spoofing detection, UAV cybersecurity, AI-based intrusion detection, blockchain-based data integrity, and swarm resilience have each been studied extensively. However, these themes are often treated as separate research problems.

Existing studies commonly focus on one of the following: improving UAV coverage or task allocation, detecting jamming or spoofing, securing communication or authentication, classifying cyberattacks using AI, preserving data integrity using blockchain, or evaluating swarm resilience under generic degradation.

A clear gap remains for an integrated defence-oriented mission-assurance framework that jointly addresses communication disruption, navigation manipulation, mission-data tampering, mission-risk estimation, adaptive mission continuation, and trustworthy mission logging.

## RA-MARS Positioning

RA-MARS is positioned as a resilient AI-driven mission assurance framework for secure multi-UAV defence surveillance in contested environments. Unlike prior studies that focus only on isolated security or optimization functions, RA-MARS integrates AI-based attack detection, mission-risk scoring, adaptive mission-continuation logic, and tamper-resistant mission logging.

The framework evaluates UAV resilience not only through attack detection accuracy but also through operational metrics such as mission success rate, packet delivery ratio, latency, energy consumption, tamper-detection rate, and mission recovery time.

## Novelty Statement

The novelty of RA-MARS lies in treating UAV security as a mission-assurance problem rather than an isolated detection, communication, navigation, or logging problem. By integrating AI-based cyber-physical attack detection with mission-risk scoring, adaptive mission continuation, and tamper-resistant logging, RA-MARS provides a unified evaluation framework for secure multi-UAV defence surveillance under jamming, GPS spoofing, and data-tampering attacks.

---

# System Model and Threat Model

## System Model

This study considers a multi-UAV defence surveillance mission conducted in a contested environment. A group of UAVs is deployed to monitor a predefined surveillance area divided into multiple mission zones. Each UAV is assigned one or more mission zones and periodically reports telemetry, navigation, communication, and mission-status information to a ground control station.

The UAV team is assumed to operate cooperatively. Each UAV may contribute to surveillance coverage, target observation, mission-zone completion, and relay communication. The ground control station monitors the mission state, receives telemetry updates, evaluates possible attack indicators, and coordinates mission-continuation decisions.

## Mission Environment

The mission area is modeled as a grid-based surveillance region. Each grid cell represents a mission zone that must be observed within the mission duration. UAVs move across assigned mission zones while transmitting telemetry at fixed intervals.

Each UAV reports:

- UAV identifier
- timestamp
- current position
- expected position
- velocity
- battery level
- packet delivery status
- communication latency
- mission-zone progress
- attack-detection state
- mission-risk score
- log-integrity status

Mission success is evaluated based on completed zone coverage, communication reliability, navigation consistency, and mission-data integrity.

## Communication Model

UAVs communicate with the ground control station through wireless links. Communication performance is represented using packet delivery ratio, packet loss rate, and latency. In normal operation, telemetry packets are delivered with high reliability and low latency.

Under adversarial conditions, communication may degrade due to RF jamming. Jamming is modeled by increasing packet loss and latency for selected UAV nodes during specific time intervals.

## Navigation Model

Each UAV follows an expected route through assigned mission zones. Navigation consistency is evaluated using route deviation, GPS position change, velocity consistency, and abnormal location jumps.

Under GPS/GNSS spoofing, false position values may be injected into UAV telemetry. Spoofing may appear as sudden jumps, gradual drift, or inconsistent movement patterns that deviate from the expected route.

## Mission Logging Model

Each UAV telemetry record is stored as part of a mission log. The mission log is used for post-mission analysis, mission accountability, and surveillance record verification.

RA-MARS uses a tamper-resistant logging model based on hash-chain or blockchain-inspired record linking. Each mission record includes the hash of the previous record and its own current hash. If any record is modified after storage, the recalculated hash will not match the stored hash, allowing tampering to be detected.

## Threat Model

The adversary is assumed to be capable of disrupting UAV communication, manipulating UAV navigation data, or modifying mission records [2,6,11,15,30,38,43]. The adversary may target individual UAVs, groups of UAVs, or mission logs.

This study considers three main attack types:

1. RF jamming
2. GPS/GNSS spoofing
3. Mission-data tampering

A combined attack scenario is also considered, where communication, navigation, and data integrity are affected at the same time.

## RF Jamming Attack

RF jamming targets the communication links between UAVs and the ground control station.

### Attack Effects

RF jamming may cause:

- increased packet loss
- increased communication latency
- missed telemetry updates
- reduced command-and-control reliability
- degraded coordination among UAVs
- lower mission success rate

### Simulation Representation

In the simulation, jamming is represented by:

- reducing packet delivery probability
- increasing latency
- affecting a subset of UAV nodes
- varying attack duration and intensity

## GPS/GNSS Spoofing Attack

GPS/GNSS spoofing targets UAV navigation and positioning trustworthiness.

### Attack Effects

GPS spoofing may cause:

- false UAV position reports
- abnormal location jumps
- gradual route drift
- velocity inconsistency
- incorrect mission-zone coverage
- mission deviation

### Simulation Representation

In the simulation, spoofing is represented by:

- injecting false x-position and y-position values
- increasing route deviation
- creating sudden GPS jumps
- creating gradual drift patterns
- affecting selected UAVs during attack intervals

## Mission-Data Tampering Attack

Mission-data tampering targets stored telemetry records, surveillance logs, or mission-status information.

### Attack Effects

Mission-data tampering may cause:

- modified UAV position records
- modified timestamps
- altered mission-zone status
- corrupted post-mission evidence
- reduced auditability and mission trustworthiness

### Simulation Representation

In the simulation, tampering is represented by:

- modifying selected mission records
- changing telemetry values after logging
- invalidating hash-chain verification
- measuring tamper-detection rate

## Combined Attack Scenario

The combined attack scenario includes RF jamming, GPS/GNSS spoofing, and mission-data tampering during the same mission.

This scenario is important because real contested environments may involve simultaneous communication disruption, navigation manipulation, and data-integrity attacks. A mission-assurance framework should therefore be evaluated not only against isolated attacks but also against combined attack conditions.

## Assumptions

The study uses the following assumptions:

- UAVs periodically transmit telemetry to the ground control station.
- The ground control station can process telemetry and mission logs.
- The adversary can affect selected UAVs but does not physically capture all UAV nodes.
- Attack effects are modeled through simulation parameters.
- UAVs operate within a predefined surveillance region.
- Mission logs can be verified using hash-chain or blockchain-inspired integrity checks.

## Limitations

The threat model does not currently include:

- physical UAV capture
- insider attacks
- malware inside UAV firmware
- advanced adversarial attacks on onboard perception models
- real RF hardware-level jamming experiments
- real UAV flight testing
- classified defence communication protocols

These limitations should be acknowledged in the final manuscript and addressed as future work.

## RA-MARS Security Objectives

RA-MARS aims to support the following security and mission-assurance objectives:

1. Detect abnormal communication, navigation, and log-integrity patterns.
2. Estimate mission risk under adversarial conditions.
3. Support adaptive mission continuation when UAVs are degraded.
4. Preserve tamper-resistant mission records.
5. Improve mission success under jamming, spoofing, and data-tampering attacks.
6. Evaluate resilience using mission-level metrics, not only attack-detection accuracy.

---

# Methodology

## Overview of RA-MARS

RA-MARS is proposed as a resilient AI-driven mission assurance framework for secure multi-UAV defence surveillance in contested environments. The framework is designed to support UAV mission continuity, attack awareness, and mission-data trustworthiness under radio-frequency jamming, GPS spoofing, and data-tampering attacks.

The methodology consists of four main modules:

1. AI-based attack detection
2. Mission-risk scoring
3. Adaptive mission-continuation logic
4. Blockchain-inspired tamper-resistant mission logging

These modules operate together to detect abnormal mission conditions, estimate the severity of operational degradation, support adaptive mission decisions, and preserve trustworthy mission records.

## System Architecture

The RA-MARS architecture includes the following components:

- Multi-UAV surveillance layer
- Ground control station
- Telemetry and communication layer
- AI-based anomaly detection module
- Mission-risk scoring module
- Adaptive mission-continuation module
- Tamper-resistant logging module
- Mission monitoring and evaluation layer

Each UAV periodically transmits telemetry information, including location, velocity, battery level, communication status, mission-zone progress, and sensor status. The ground control station receives UAV telemetry and evaluates whether mission behavior is normal or potentially affected by adversarial conditions.

## Multi-UAV Surveillance Layer

The multi-UAV surveillance layer represents a coordinated UAV team assigned to monitor a defence surveillance area. The mission area is divided into multiple grid-based zones. Each UAV is assigned one or more zones and periodically reports telemetry and mission status to the ground control station.

The surveillance mission is considered successful when a predefined percentage of mission zones is covered within the mission duration while maintaining acceptable communication reliability and navigation consistency.

## Threat Model

RA-MARS considers three major attack types:

### RF Jamming
RF jamming disrupts UAV communication by increasing packet loss and communication latency. In the simulation, jamming is modeled by reducing packet delivery ratio and increasing communication delay for affected UAV nodes.

### GPS Spoofing
GPS spoofing manipulates UAV navigation by injecting false location values. In the simulation, spoofing is modeled through abnormal location jumps, gradual position drift, and inconsistent movement patterns.

### Data Tampering
Data tampering modifies mission telemetry records or surveillance logs after collection. In the simulation, tampering is modeled by altering selected records, including location values, timestamps, mission status, or UAV identifiers.

## AI-Based Attack Detection Module

The AI-based attack detection module classifies mission states as normal or attacked based on UAV telemetry and mission-status features.

### Input Features

The detection module uses the following features:

- Packet delivery ratio
- Average communication latency
- GPS position change
- Velocity consistency
- Route deviation
- Battery drain rate
- Mission progress rate
- Log integrity status

### Output Classes

The model may classify mission states into the following classes:

- Normal
- Jamming
- GPS spoofing
- Data tampering
- Combined attack

### Candidate Models

The following machine-learning models can be evaluated:

- Logistic Regression
- Support Vector Machine
- Random Forest
- Gradient Boosting or XGBoost
- Lightweight Neural Network

The best-performing model can be selected based on accuracy, precision, recall, and F1-score.

## Mission-Risk Scoring Module

The mission-risk scoring module estimates the severity of the current mission condition using AI detection results and operational indicators.

A simple mission-risk score can be defined using weighted factors:

Risk Score = w1(attack probability) + w2(packet loss rate) + w3(route deviation) + w4(latency increase) + w5(log integrity violation)

Where:
- attack probability is the predicted probability from the AI detection model
- packet loss rate indicates communication degradation
- route deviation indicates navigation inconsistency
- latency increase indicates command-and-control delay
- log integrity violation indicates possible data tampering
- w1 to w5 are weighting coefficients

The risk score can be categorized as:

| Risk Level | Score Range | Action |
|---|---|---|
| Low | 0.00–0.30 | Continue normal mission |
| Medium | 0.31–0.60 | Increase monitoring and verify mission data |
| High | 0.61–0.80 | Trigger adaptive mission continuation |
| Critical | 0.81–1.00 | Reassign mission zone or return affected UAV |

## Adaptive Mission-Continuation Logic

The adaptive mission-continuation module determines how the UAV team should respond when risk increases.

Possible adaptive actions include:

- Continue normal operation
- Increase monitoring frequency
- Reassign affected mission zones to nearby UAVs
- Reroute UAVs around high-risk zones
- Reduce dependence on affected UAVs
- Trigger return-to-base action for critically affected UAVs

The purpose of this module is not only to detect attacks but also to preserve mission success under degraded conditions.

## Tamper-Resistant Mission Logging Module

The tamper-resistant logging module preserves the integrity and traceability of mission records using ideas related to secure UAV logging, lightweight blockchain, and data-provenance systems [15–19]. Each mission record is linked to the previous record using a hash-chain or blockchain-inspired structure.

Each record may include:

- UAV ID
- Timestamp
- Location
- Mission-zone status
- Communication status
- Attack detection status
- Risk score
- Previous record hash
- Current record hash

If any record is modified after storage, the recalculated hash will not match the stored hash. This allows tampered records to be detected during verification.

## RA-MARS Workflow

The RA-MARS workflow follows these steps:

1. UAVs collect telemetry and mission-status data.
2. Telemetry is transmitted to the ground control station.
3. The AI module evaluates whether the mission state is normal or attacked.
4. The mission-risk scoring module calculates the risk level.
5. The adaptive mission-continuation module selects an appropriate response.
6. Mission records are stored using tamper-resistant logging.
7. Performance metrics are calculated for evaluation.

## Evaluation Strategy

RA-MARS will be evaluated under five scenarios:

1. Normal operation
2. RF jamming attack
3. GPS spoofing attack
4. Data-tampering attack
5. Combined attack scenario

The framework will be compared against:

- Conventional UAV system
- AI-only detection system
- Logging-only system
- Non-adaptive secure system
- Proposed RA-MARS framework

## Evaluation Metrics

The evaluation will use the following metrics:

- Mission success rate
- Attack detection accuracy
- Precision
- Recall
- F1-score
- Packet delivery ratio
- Average latency
- Energy consumption
- Tamper-detection rate
- Mission recovery time

## Methodological Positioning

RA-MARS should be presented as a simulation-based defence mission-assurance framework. The paper should not claim real-world deployment or military-grade validation unless supported by field testing. The contribution should focus on integrated mission assurance, comparative simulation, and operational resilience under contested conditions.

---

# Experimental Setup

## Overview

This section describes the simulation-based evaluation setup for RA-MARS. The purpose of the experiment is to evaluate whether the proposed framework improves mission assurance for multi-UAV defence surveillance under normal and adversarial conditions.

The evaluation is designed around five mission scenarios:

1. Normal operation
2. RF jamming attack
3. GPS/GNSS spoofing attack
4. Mission-data tampering attack
5. Combined attack scenario

RA-MARS is compared against multiple baseline systems using attack-detection, communication, navigation, integrity, energy, and mission-level performance metrics.

## Simulation Environment

The simulation is designed as a Python-based discrete mission simulation. The mission area is represented as a grid-based surveillance region, and UAVs are assigned to cover predefined mission zones.

The simulation generates synthetic UAV telemetry data and attack events. The generated dataset is used to train and evaluate AI-based attack detection models and to compare RA-MARS with baseline systems.

## Mission Scenario

The mission scenario represents a multi-UAV defence surveillance operation in a contested environment.

The mission includes:

- a 5 km × 5 km surveillance region
- 25 grid-based mission zones
- 10, 20, and 30 UAV configurations
- one ground control station
- periodic telemetry transmission
- route-following and zone-coverage objectives
- adversarial attack injection during mission execution

Each UAV is assigned one or more zones and must report telemetry at fixed intervals. Mission success is measured based on completed zone coverage, communication reliability, navigation consistency, and mission-data integrity.

## Simulation Parameters

| Parameter | Value |
|---|---:|
| Simulation area | 5 km × 5 km |
| Mission zones | 25 |
| UAV configurations | 10, 20, and 30 UAVs |
| Ground control station | 1 |
| Simulation duration | 600 seconds |
| Telemetry interval | 1 second |
| Runs per scenario | 30 |
| UAV speed | 10–25 m/s |
| Communication range | 500–1000 m |
| Initial battery | 100% |

## Attack Scenarios

### Scenario 1: Normal Operation

No attack is applied. UAVs perform surveillance, transmit telemetry, and update mission logs under normal operating conditions.

### Scenario 2: RF Jamming

RF jamming is modeled by increasing packet loss and communication latency for selected UAVs.

Jamming parameters include:

- attack start time
- attack duration
- affected UAV ratio
- packet loss intensity
- additional latency

### Scenario 3: GPS/GNSS Spoofing

GPS/GNSS spoofing is modeled by injecting false position values into UAV telemetry.

Spoofing effects include:

- sudden location jumps
- gradual position drift
- route deviation
- velocity inconsistency
- incorrect mission-zone reporting

### Scenario 4: Mission-Data Tampering

Mission-data tampering is modeled by modifying selected telemetry records after logging.

Tampering effects include:

- changed UAV coordinates
- modified timestamps
- altered mission-zone status
- broken hash-chain verification

### Scenario 5: Combined Attack

The combined attack scenario applies RF jamming, GPS/GNSS spoofing, and mission-data tampering within the same mission. This scenario evaluates the ability of RA-MARS to support mission assurance under simultaneous cyber-electromagnetic and data-integrity threats.

## Baseline Systems

RA-MARS is compared against four baseline systems.

| Baseline | Description |
|---|---|
| B1: Conventional UAV System | No AI detection, no risk scoring, no adaptive response, and no tamper-resistant logging |
| B2: AI-Only Detection System | Uses AI detection but does not include risk scoring, adaptive logic, or tamper-resistant logging |
| B3: Logging-Only System | Uses tamper-resistant logging but does not include AI detection or adaptive mission logic |
| B4: Non-Adaptive Secure System | Uses AI detection, risk scoring, and logging, but does not perform adaptive mission continuation |
| B5: RA-MARS | Uses AI detection, mission-risk scoring, adaptive mission logic, and tamper-resistant logging |

## AI Detection Models

The AI detection module classifies UAV mission states into cyber-physical attack categories, following prior UAV IDS and anomaly-detection studies [25–29].

- normal
- jamming
- spoofing
- tampering
- combined attack

Candidate models include:

- Logistic Regression
- Support Vector Machine
- Random Forest
- Gradient Boosting or XGBoost
- Lightweight Neural Network

The best-performing model is selected based on accuracy, precision, recall, and F1-score.

## Input Features

The AI detection module uses telemetry, communication, navigation, and integrity features.

| Feature | Description |
|---|---|
| packet_delivery_ratio | Communication reliability |
| latency_ms | Communication delay |
| packet_loss_rate | Communication degradation |
| route_deviation | Navigation deviation from expected path |
| gps_jump | Abnormal location change |
| velocity_inconsistency | Difference between expected and observed movement |
| battery_drain_rate | Energy degradation pattern |
| mission_progress_rate | Mission-zone completion progress |
| log_integrity_status | Whether the mission record passes integrity verification |

## Evaluation Metrics

The evaluation uses the following metrics:

| Metric | Purpose |
|---|---|
| Mission success rate | Measures completed surveillance coverage |
| Attack detection accuracy | Measures correct classification of mission state |
| Precision | Measures reliability of predicted attacks |
| Recall | Measures ability to detect actual attacks |
| F1-score | Balances precision and recall |
| Packet delivery ratio | Measures communication reliability |
| Average latency | Measures communication delay |
| Route deviation | Measures navigation trustworthiness |
| Tamper-detection rate | Measures mission-log integrity verification |
| Energy consumption | Measures operational overhead |
| Mission recovery time | Measures adaptive response effectiveness |

## Experimental Procedure

The evaluation follows these steps:

1. Generate synthetic UAV mission data for each scenario.
2. Inject attack effects according to the defined attack model.
3. Train AI detection models using the generated dataset.
4. Evaluate attack classification performance.
5. Compute mission-risk scores.
6. Apply adaptive mission-continuation logic in RA-MARS.
7. Verify mission logs using tamper-resistant logging.
8. Compare RA-MARS against baseline systems.
9. Generate result tables and graphs.
10. Interpret the findings from a mission-assurance perspective.

## Result Files

The simulation should generate the following result files:

| File | Purpose |
|---|---|
| synthetic_uav_mission_data.csv | Full generated telemetry dataset |
| model_performance.csv | AI detection results |
| mission_success_results.csv | Mission success comparison |
| communication_results.csv | Packet delivery and latency results |
| navigation_results.csv | Route deviation and spoofing results |
| tamper_detection_results.csv | Mission-log integrity results |
| energy_results.csv | Energy consumption results |
| recovery_time_results.csv | Mission recovery results |
| ablation_results.csv | RA-MARS module contribution results |

## Research Integrity Statement

All numerical values used in the final manuscript must be generated from the simulation code. The synthetic dataset should be clearly described as simulation-generated UAV telemetry data and should not be presented as real military flight data.

The results should be interpreted as simulation-based evidence of mission-assurance improvement under controlled attack scenarios. Real-world flight testing and hardware-in-the-loop validation are left for future work.

---

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

---

# Limitations and Future Work

## Limitations

Although RA-MARS is designed to improve mission assurance for multi-UAV defence surveillance under contested conditions, this study has several limitations.

First, the evaluation is simulation-based. The UAV telemetry data, attack events, mission-zone coverage, and adversarial conditions are generated through controlled simulation. Therefore, the results should be interpreted as simulation-based evidence rather than real-world flight validation.

Second, the attack models are simplified representations of RF jamming, GPS/GNSS spoofing, and mission-data tampering. Real contested environments may involve more complex electromagnetic interference, adaptive jammers, multipath effects, stealthy spoofing strategies, insider threats, malware, and coordinated adversarial behavior.

Third, the proposed tamper-resistant logging module is modeled using a lightweight hash-chain or blockchain-inspired structure. While this approach supports mission-record integrity verification, the study does not claim full-scale deployment of a production blockchain network in operational defence UAV systems.

Fourth, the simulation does not include physical UAV capture, hardware compromise, firmware-level malware, classified defence communication protocols, or real electronic warfare hardware. These factors may significantly affect system performance in real operational environments.

Fifth, the proposed AI-based detection module depends on the quality and representativeness of the generated telemetry and attack data. Real-world attack patterns may differ from the synthetic scenarios used in this study.

Finally, the framework focuses on mission assurance for surveillance-oriented multi-UAV operations. Additional validation would be required before applying the framework to other defence missions such as strike coordination, logistics, electronic attack, or manned-unmanned teaming.

## Future Work

Future work may extend RA-MARS in several directions.

First, hardware-in-the-loop and real UAV flight experiments can be conducted to validate the framework under more realistic communication, navigation, and mission-control conditions.

Second, future studies can incorporate more advanced adversarial models, including adaptive jamming, coordinated spoofing, adversarial machine learning attacks, malware-based telemetry manipulation, and insider threats.

Third, the tamper-resistant logging module can be extended using lightweight distributed ledger architectures optimized for resource-constrained UAV swarms.

Fourth, RA-MARS can be evaluated with larger swarm sizes, heterogeneous UAV platforms, and cross-domain autonomous systems involving air, ground, and maritime agents.

Fifth, the AI detection module can be improved using federated learning, online learning, continual learning, and uncertainty-aware models to support adaptation under changing mission environments.

Finally, future work can investigate human-machine teaming interfaces that allow operators to interpret RA-MARS risk scores, mission alerts, and adaptive response recommendations in real time.

---

# Conclusion

This paper proposed RA-MARS, a resilient AI-driven mission assurance framework for secure multi-UAV defence surveillance in contested environments. The framework addresses three major adversarial conditions affecting UAV operations: radio-frequency jamming, GPS/GNSS spoofing, and mission-data tampering.

Unlike approaches that focus only on isolated attack detection, secure communication, or data integrity, RA-MARS integrates AI-based attack detection, mission-risk scoring, adaptive mission-continuation logic, and blockchain-inspired tamper-resistant mission logging into a unified mission-assurance workflow. This integrated approach is designed to improve not only attack awareness but also operational continuity, communication reliability, navigation trustworthiness, and mission-data integrity.

The v2 simulation evaluation used synthetic multi-UAV telemetry data with row-level attack labels and non-leakage telemetry features. The best-performing AI model, Gradient Boosting, achieved 89.87% accuracy, 90.50% macro precision, 89.86% macro recall, and 89.71% macro F1-score. At the mission level, RA-MARS improved mission success under the combined attack scenario from 63.21% for the conventional UAV baseline to 78.60%. It also improved packet delivery ratio from 0.761 to 0.885, reduced average route deviation from 67.32 m to 48.00 m, and reduced mission recovery time from 117.64 s to 67.97 s.

These results suggest that multi-UAV resilience should be evaluated from a mission-assurance perspective rather than only through attack-classification accuracy. Detection alone is not sufficient for defence surveillance missions. A resilient UAV framework must also estimate mission risk, support adaptive mission continuation, and preserve trustworthy mission records.

The study has several limitations. The evaluation is simulation-based and uses synthetic UAV telemetry data rather than real military flight data. The attack models are controlled abstractions of jamming, spoofing, and tampering rather than full hardware-level electronic warfare experiments. Future work should include hardware-in-the-loop validation, real UAV flight testing, adaptive adversarial attack models, larger heterogeneous UAV swarms, and human-machine teaming interfaces for mission-risk interpretation and operator decision support.

---

# Data Availability Statement

The data used in this study will be generated through a Python-based simulation of multi-UAV defence surveillance under normal and adversarial mission conditions.

The generated dataset will consist of synthetic UAV telemetry records, mission-status information, communication indicators, navigation-deviation features, attack labels, mission-risk scores, and log-integrity indicators.

The dataset will not contain real military UAV flight data, classified defence information, personal information, or operationally sensitive mission records.

Simulation scripts and generated non-sensitive synthetic datasets may be made available upon reasonable request or through a public repository, subject to journal requirements and author discretion.

# Code Availability Statement

The simulation code will be developed in Python and used to generate synthetic UAV telemetry data, attack scenarios, AI detection results, mission-risk scores, and performance metrics.

The code may be made available in a GitHub repository after the manuscript reaches a suitable preprint or publication stage.

# Synthetic Data Statement

This study uses simulation-generated synthetic data for controlled experimental evaluation. The data should not be interpreted as real-world UAV flight data or operational military mission data.
