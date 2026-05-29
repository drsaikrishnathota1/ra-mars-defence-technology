# Related Work

## Overview

This section reviews prior work related to multi-UAV defence surveillance, UAV mission assurance, AI-based attack detection, RF jamming, GPS spoofing, UAV cybersecurity, and tamper-resistant mission logging. The purpose of this section is to identify the research gap that motivates RA-MARS.

## UAV Defence Surveillance and Reconnaissance

Unmanned aerial vehicles have become important platforms for defence surveillance, reconnaissance, border monitoring, battlefield awareness, and critical-infrastructure protection. Multi-UAV systems provide advantages over single-UAV platforms because they can cover larger mission areas, improve redundancy, and support distributed sensing.

Prior studies have explored UAV-based surveillance for target monitoring, battlefield situational awareness, search operations, and autonomous reconnaissance. However, many of these studies focus primarily on mission planning, perception, or coverage optimization. Less attention is given to how UAV surveillance missions can remain operationally reliable when communication, navigation, and mission data are attacked simultaneously.

## Multi-UAV Mission Planning and Mission Assurance

Multi-UAV mission planning research commonly focuses on path planning, task allocation, coverage optimization, and energy-efficient coordination. These studies are important for improving mission efficiency, but many assume relatively stable communication and navigation conditions.

Mission assurance requires a broader perspective. In defence environments, the goal is not only to complete a planned route but also to continue the mission under degraded, uncertain, or adversarial conditions. Existing mission-planning approaches often do not integrate attack detection, mission-risk scoring, adaptive continuation, and trustworthy logging into a single framework.

## RF Jamming Detection and Anti-Jamming in UAV Networks

RF jamming is a serious threat to UAV communication because it can reduce packet delivery ratio, increase latency, and disrupt command-and-control communication. Prior work has studied jamming detection, anti-jamming communication, frequency hopping, reinforcement learning-based channel selection, and resilient UAV networking.

Although these studies improve communication resilience, many focus mainly on communication metrics. They often do not connect jamming detection to broader mission-assurance outcomes such as mission success rate, recovery time, or adaptive mission continuation.

## GPS Spoofing Detection in UAV Systems

GPS spoofing can manipulate UAV navigation by injecting false location information. This can cause route deviation, mission failure, loss of formation, or unsafe UAV behavior. Existing studies have explored spoofing detection using sensor fusion, signal analysis, inertial navigation comparison, machine learning, and anomaly detection.

However, many GPS spoofing studies focus primarily on detecting false location information. In defence surveillance missions, spoofing detection should also be connected to mission risk, route reassignment, operational continuity, and post-mission data trustworthiness.

## AI-Based Anomaly Detection in UAV and Cyber-Physical Systems

AI and machine learning methods have been widely used for anomaly detection in UAV networks, cyber-physical systems, and communication systems. Common approaches include logistic regression, support vector machines, random forests, gradient boosting, deep neural networks, and autoencoder-based models.

These methods can identify abnormal communication, navigation, or system behavior. However, AI-based detection alone may not be sufficient for defence mission assurance. A system may detect an attack but still fail to preserve mission continuity if detection outputs are not connected to mission-risk scoring and adaptive response mechanisms.

## UAV Cybersecurity and Secure Communication

UAV cybersecurity research has examined secure communication, authentication, intrusion detection, data confidentiality, and cyber-physical attack mitigation. These studies are relevant because UAV systems depend on reliable communication links, trusted telemetry, and secure control channels.

However, many UAV cybersecurity approaches focus on protecting individual security properties such as confidentiality, authentication, or intrusion detection. Defence mission assurance requires a more integrated approach that combines security monitoring, operational resilience, and mission-data integrity.

## Blockchain and Tamper-Resistant Logging for UAV Data Integrity

Blockchain and hash-chain techniques have been studied for UAV data integrity, secure logging, provenance tracking, and auditability. These methods can help detect unauthorized modification of telemetry records, surveillance data, and mission logs.

However, blockchain-based UAV studies sometimes focus heavily on data storage and integrity while underemphasizing real-time mission performance. In defence surveillance, tamper-resistant logging should support mission assurance without creating unacceptable latency, energy, or communication overhead.

## Research Gap

The reviewed literature shows that UAV surveillance, jamming detection, GPS spoofing detection, AI-based anomaly detection, UAV cybersecurity, and tamper-resistant logging have often been studied as separate problems. However, multi-UAV defence surveillance missions in contested environments may face multiple simultaneous threats that affect communication reliability, navigation trustworthiness, mission continuity, and mission-data integrity.

There remains a need for an integrated mission-assurance framework that jointly addresses attack detection, mission-risk estimation, adaptive mission continuation, and tamper-resistant mission logging.

## Positioning of RA-MARS

RA-MARS is positioned as a defence-oriented mission assurance framework for secure multi-UAV surveillance in contested environments. Unlike approaches that focus only on detection, communication security, or data integrity, RA-MARS integrates AI-based attack detection, mission-risk scoring, adaptive mission-continuation logic, and blockchain-inspired tamper-resistant logging into a unified workflow.

This integrated approach enables evaluation not only through attack detection accuracy but also through operational metrics such as mission success rate, packet delivery ratio, latency, energy consumption, tamper-detection rate, and mission recovery time.
