# RA-MARS Threat Model Figure Plan

## Purpose
This file documents the threat model for the RA-MARS manuscript. The goal is to clearly define the adversarial conditions considered in the study.

## Figure Title
Threat Model for Multi-UAV Defence Surveillance in Contested Environments

## System Components

The threat model includes the following components:

- Multi-UAV team
- Ground control station
- Wireless communication links
- GPS/GNSS navigation signals
- Mission telemetry records
- Mission logs
- Surveillance mission zones

## Adversary Capabilities

The adversary is assumed to have the ability to disrupt, manipulate, or tamper with selected UAV mission components.

The adversary may:

1. Jam UAV communication links
2. Spoof GPS/GNSS navigation information
3. Tamper with mission telemetry records
4. Modify mission logs after collection
5. Launch combined attacks affecting communication, navigation, and data integrity

## Threat 1: RF Jamming

### Target
Wireless communication links between UAVs and the ground control station.

### Attack Effect
RF jamming may cause:

- Increased packet loss
- Increased communication latency
- Loss of command-and-control reliability
- Reduced telemetry availability
- Mission coordination disruption

### RA-MARS Response
RA-MARS detects jamming indicators using communication features such as packet delivery ratio, latency, and communication degradation patterns.

## Threat 2: GPS/GNSS Spoofing

### Target
UAV navigation and positioning data.

### Attack Effect
GPS/GNSS spoofing may cause:

- False UAV position reports
- Route deviation
- Incorrect mission-zone coverage
- Formation disruption
- Navigation inconsistency

### RA-MARS Response
RA-MARS detects spoofing indicators using location jumps, velocity inconsistency, abnormal route deviation, and mission-zone mismatch.

## Threat 3: Mission-Data Tampering

### Target
Mission telemetry records, surveillance records, and mission logs.

### Attack Effect
Data tampering may cause:

- Altered UAV location records
- Modified timestamps
- Changed mission-zone status
- Corrupted post-mission evidence
- Reduced command accountability

### RA-MARS Response
RA-MARS uses hash-chain or blockchain-inspired tamper-resistant logging to detect unauthorized modification of mission records.

## Threat 4: Combined Attack Scenario

### Target
Communication, navigation, and mission-data integrity at the same time.

### Attack Effect
Combined attacks may cause:

- Communication degradation
- Navigation manipulation
- Mission record corruption
- Reduced mission success
- Increased recovery time

### RA-MARS Response
RA-MARS combines AI-based attack detection, mission-risk scoring, adaptive mission continuation, and tamper-resistant logging to support mission assurance.

## Assumptions

The study assumes:

- UAVs periodically transmit telemetry to the ground control station.
- The ground control station can process telemetry and mission records.
- Attack effects can be modeled through simulation parameters.
- The adversary can affect selected UAVs but does not physically capture all UAV nodes.
- The framework is evaluated using simulation, not real flight testing.

## Limitations

The threat model does not currently include:

- Physical UAV capture
- Insider attacks
- Full malware infection of UAV firmware
- Advanced adversarial AI attacks on image recognition models
- Real RF hardware-level signal processing
- Real battlefield deployment testing

These can be listed as future work.

## Suggested Figure Layout

Recommended visual layout:

- Center: UAV swarm and mission area
- Bottom: ground control station
- Left side: RF jammer attacking communication links
- Top side: GPS/GNSS spoofing source attacking navigation signals
- Right side: data-tampering attacker targeting mission logs
- Bottom-right: RA-MARS response modules

## Figure Labels

Use short labels:

- RF Jamming
- GPS Spoofing
- Data Tampering
- Combined Attack
- UAV Swarm
- Ground Control Station
- Mission Logs
- RA-MARS Detection
- Risk Scoring
- Adaptive Response
- Tamper-Resistant Logging

## Figure Caption Draft

Figure 2. Threat model for multi-UAV defence surveillance in contested environments. The adversary may disrupt UAV communication through RF jamming, manipulate navigation using GPS/GNSS spoofing, or modify mission records through data-tampering attacks. RA-MARS addresses these threats using AI-based detection, mission-risk scoring, adaptive mission-continuation logic, and tamper-resistant mission logging.
