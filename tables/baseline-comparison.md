# Baseline Comparison Plan

## Target Journal
Defence Technology

## Study Title
RA-MARS: A Resilient AI-Driven Mission Assurance Framework for Secure Multi-UAV Defence Surveillance Under Jamming, GPS Spoofing, and Data-Tampering Attacks

## Purpose
This file defines the baseline systems that will be compared against the proposed RA-MARS framework. Strong baseline comparison is important because Defence Technology rejected the earlier manuscript for insufficient novelty. The baselines help show that RA-MARS provides measurable improvement over simpler or partial approaches.

## Baseline Summary

| Method | AI Attack Detection | Mission-Risk Scoring | Adaptive Mission Logic | Tamper-Resistant Logging | Purpose |
|---|---|---|---|---|---|
| B1: Conventional UAV System | No | No | No | No | Represents a basic UAV surveillance system without advanced resilience features |
| B2: AI-Only Detection System | Yes | No | No | No | Tests whether detection alone is enough to improve mission assurance |
| B3: Logging-Only System | No | No | No | Yes | Tests whether tamper-resistant logging alone improves data trustworthiness |
| B4: Non-Adaptive Secure System | Yes | Yes | No | Yes | Tests a secure system that detects risk but does not adapt mission behavior |
| B5: Proposed RA-MARS | Yes | Yes | Yes | Yes | Full proposed framework |

## B1: Conventional UAV System

### Description
The conventional UAV system represents a standard multi-UAV surveillance setup without AI-based attack detection, mission-risk scoring, adaptive mission continuation, or tamper-resistant logging.

### Included Features
- UAV mission execution
- Telemetry transmission
- Basic mission logging
- Fixed route or zone coverage plan

### Missing Features
- No AI-based anomaly detection
- No risk scoring
- No adaptive mission continuation
- No tamper-resistant log verification

### Expected Weakness
This baseline is expected to perform poorly under jamming, GPS spoofing, and data-tampering attacks because it cannot identify attacks or adapt mission behavior.

## B2: AI-Only Detection System

### Description
The AI-only detection baseline uses machine learning to classify normal and attack conditions. However, it does not include mission-risk scoring, adaptive mission decisions, or tamper-resistant logging.

### Included Features
- AI-based anomaly detection
- Classification of normal, jamming, spoofing, and tampering indicators

### Missing Features
- No mission-risk scoring
- No adaptive mission-continuation logic
- No tamper-resistant mission logging

### Expected Weakness
This baseline may detect attacks but may not improve mission success because detection is not connected to mission adaptation or trustworthy logging.

## B3: Logging-Only System

### Description
The logging-only baseline uses hash-chain or blockchain-inspired tamper-resistant logging to detect changes in mission records. However, it does not include AI-based attack detection or mission adaptation.

### Included Features
- Hash-based mission logging
- Tamper detection for altered logs
- Basic audit trail

### Missing Features
- No AI-based attack detection
- No jamming or spoofing awareness
- No mission-risk scoring
- No adaptive mission-continuation logic

### Expected Weakness
This baseline can detect data tampering but cannot respond to real-time communication or navigation attacks.

## B4: Non-Adaptive Secure System

### Description
The non-adaptive secure baseline includes AI-based attack detection, mission-risk scoring, and tamper-resistant logging. However, it does not change mission behavior after detecting threats.

### Included Features
- AI-based attack detection
- Mission-risk scoring
- Tamper-resistant mission logging

### Missing Features
- No adaptive route adjustment
- No mission replanning
- No recovery strategy under attack

### Expected Weakness
This baseline can identify threats and preserve data integrity, but mission performance may still degrade because it lacks adaptive response.

## B5: Proposed RA-MARS Framework

### Description
RA-MARS integrates AI-based attack detection, mission-risk scoring, adaptive mission-continuation logic, and tamper-resistant logging into a unified defence-oriented mission assurance framework.

### Included Features
- AI-based attack detection
- Mission-risk scoring
- Adaptive mission-continuation logic
- Tamper-resistant mission logging
- Multi-threat evaluation under jamming, spoofing, tampering, and combined attacks

### Expected Strength
RA-MARS is expected to improve mission success, attack awareness, communication resilience, and data trustworthiness compared with all baseline systems.

## Comparison Metrics

| Metric | B1 | B2 | B3 | B4 | RA-MARS |
|---|---|---|---|---|---|
| Mission success rate | Expected low under attack | Medium | Low to medium | Medium | Highest |
| Attack detection accuracy | Not available | High | Not available | High | High |
| Packet delivery ratio | Low under jamming | Low to medium | Low | Medium | Higher |
| GPS spoofing detection | No | Yes | No | Yes | Yes |
| Tamper-detection rate | Low | Low | High | High | High |
| Latency overhead | Lowest | Low | Medium | Medium | Medium |
| Energy consumption | Lowest | Medium | Medium | Medium | Medium |
| Mission recovery time | Poor | Poor | Poor | Medium | Best |

## Hypothesis

The proposed RA-MARS framework is expected to outperform partial baselines because it connects detection, risk assessment, adaptive decision-making, and tamper-resistant logging into one mission-assurance workflow.

## Important Note
The paper should not claim that RA-MARS is superior without simulation evidence. The final results must support each claim using measurable metrics and fair baseline comparisons.
