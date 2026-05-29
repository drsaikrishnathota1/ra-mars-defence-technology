# RA-MARS System Architecture Figure Plan

## Purpose
This file documents the planned system architecture for RA-MARS before creating the final manuscript figure.

## Figure Title
RA-MARS System Architecture for Secure Multi-UAV Defence Surveillance

## Main Architecture Layers

### Layer 1: Multi-UAV Surveillance Layer
This layer contains the UAV team operating in a defence surveillance area.

Components:
- UAV-1, UAV-2, UAV-3, ..., UAV-N
- Mission zones
- Surveillance sensors
- UAV telemetry collection
- UAV battery and status monitoring

Data generated:
- Location
- Velocity
- Battery level
- Mission-zone status
- Communication status
- Sensor status
- Timestamped telemetry

### Layer 2: Communication and Telemetry Layer
This layer represents the communication link between UAVs and the ground control station.

Components:
- Wireless UAV communication links
- Telemetry transmission
- Command-and-control messages
- Packet delivery monitoring
- Latency monitoring

Threats affecting this layer:
- RF jamming
- Packet loss
- Communication delay
- Link disruption

### Layer 3: Ground Control and Mission Monitoring Layer
This layer receives UAV telemetry and monitors mission progress.

Components:
- Ground control station
- Mission status dashboard
- Telemetry receiver
- Mission-zone coverage tracker
- UAV health monitor

### Layer 4: AI-Based Attack Detection Layer
This layer detects abnormal mission conditions.

Inputs:
- Packet delivery ratio
- Average latency
- GPS position change
- Velocity consistency
- Route deviation
- Battery drain rate
- Mission progress rate
- Log integrity status

Outputs:
- Normal
- Jamming
- GPS spoofing
- Data tampering
- Combined attack
- Attack probability score

### Layer 5: Mission-Risk Scoring Layer
This layer converts attack detection outputs and operational indicators into a mission-risk score.

Risk factors:
- Attack probability
- Packet loss rate
- Latency increase
- Route deviation
- Battery degradation
- Log integrity violation

Risk levels:
- Low
- Medium
- High
- Critical

### Layer 6: Adaptive Mission-Continuation Layer
This layer decides how the UAV mission should continue under attack.

Possible decisions:
- Continue normal mission
- Increase monitoring frequency
- Reassign mission zone
- Reroute UAV
- Reduce reliance on affected UAV
- Return affected UAV to base
- Trigger mission recovery protocol

### Layer 7: Tamper-Resistant Mission Logging Layer
This layer records mission data in a hash-chain or blockchain-inspired structure.

Logged data:
- UAV ID
- Timestamp
- Location
- Mission status
- Communication status
- Attack status
- Risk score
- Previous hash
- Current hash

Purpose:
- Improve mission-data integrity
- Detect altered mission records
- Support post-mission auditability
- Improve operational trustworthiness

## Threat Inputs to Show in Figure

The architecture figure should visibly show three threat inputs:

1. RF jamming attack targeting communication links
2. GPS spoofing attack targeting UAV navigation data
3. Data-tampering attack targeting mission logs

## Suggested Figure Flow

UAV Team  
→ Telemetry and Communication Layer  
→ Ground Control Station  
→ AI-Based Attack Detection  
→ Mission-Risk Scoring  
→ Adaptive Mission Continuation  
→ Tamper-Resistant Mission Logging  
→ Mission Assurance Output

## Final Output of RA-MARS

The final output should show:

- Improved mission continuity
- Attack awareness
- Communication resilience
- Navigation trustworthiness
- Tamper-resistant mission records
- Defence mission assurance

## Visual Design Notes

The final figure should be clean and publication-style.

Recommended layout:
- Left side: UAV swarm and mission area
- Middle: communication and ground control station
- Right side: RA-MARS modules
- Bottom: tamper-resistant logging chain
- Top or side: adversarial threats

Avoid:
- Too many colors
- Too much text
- Cartoon-style icons
- Military symbols that look unrealistic
- Overcrowded arrows

## Figure Caption Draft

Figure 1. RA-MARS system architecture for resilient multi-UAV defence surveillance in contested environments. The framework integrates UAV telemetry collection, AI-based attack detection, mission-risk scoring, adaptive mission-continuation logic, and tamper-resistant mission logging to support mission assurance under RF jamming, GPS spoofing, and data-tampering attacks.
