# Results and Discussion

## Overview

This section will present the simulation results for the RA-MARS framework. The results will compare the proposed framework with baseline systems under normal operation, RF jamming, GPS spoofing, data-tampering, and combined attack scenarios.

At this stage, this file provides the planned structure for the results section. Final numerical values should be added only after simulation is completed.

## Evaluation Scenarios

The following scenarios will be evaluated:

1. Normal operation
2. RF jamming attack
3. GPS spoofing attack
4. Data-tampering attack
5. Combined attack scenario

Each scenario should be tested using multiple simulation runs to improve reliability of the results.

## Baseline Methods

The proposed RA-MARS framework will be compared against the following baselines:

- Conventional UAV surveillance system
- AI-only attack detection system
- Logging-only system
- Non-adaptive secure system
- Proposed RA-MARS framework

## Attack Detection Performance

This subsection will report the performance of AI-based attack detection models.

Metrics to include:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

Models to compare:

- Logistic Regression
- Support Vector Machine
- Random Forest
- Gradient Boosting or XGBoost
- Lightweight Neural Network

Discussion should explain which model performs best and why it is suitable for the RA-MARS detection module.

## Mission Success Rate

This subsection will compare mission success rate across all baseline systems and attack scenarios.

Mission success rate should measure the percentage of mission zones successfully covered within the mission duration.

Expected discussion points:

- How jamming affects mission completion
- How GPS spoofing causes route deviation
- How combined attacks reduce mission effectiveness
- Whether RA-MARS improves mission continuity compared with baselines
- Whether adaptive mission-continuation logic improves mission recovery

## Communication Performance

This subsection will discuss packet delivery ratio and average latency.

Metrics to include:

- Packet delivery ratio
- Average latency
- Communication degradation under jamming
- Recovery after adaptive response

Expected discussion points:

- Conventional systems may show reduced packet delivery under jamming
- AI-only detection may identify attacks but may not improve delivery
- RA-MARS may improve mission-level communication resilience through adaptive mission logic
- Any added latency from security and logging modules should be reported honestly

## GPS Spoofing Detection and Navigation Reliability

This subsection will discuss how well the system detects GPS spoofing and limits navigation degradation.

Metrics to include:

- Spoofing detection accuracy
- Route deviation
- Mission-zone completion rate
- Recovery time after spoofing detection

Expected discussion points:

- GPS spoofing can create abnormal location jumps or gradual drift
- AI-based detection can identify inconsistent movement patterns
- Mission-risk scoring can help determine whether a UAV should continue, reroute, or transfer mission responsibility

## Tamper-Detection Performance

This subsection will evaluate the tamper-resistant logging module.

Metrics to include:

- Number of tampered records
- Number of detected tampered records
- Tamper-detection rate
- Verification time
- Logging overhead

Expected discussion points:

- Conventional logs may not detect post-mission modification
- Hash-chain or blockchain-inspired logging can detect altered records
- RA-MARS links tamper detection with mission assurance and operational trust
- Logging overhead should be discussed carefully

## Energy Consumption and Operational Overhead

This subsection will report the energy and computational overhead caused by AI detection, adaptive logic, and tamper-resistant logging.

Metrics to include:

- Battery consumption
- Communication overhead
- Logging overhead
- Security-processing overhead

Expected discussion points:

- RA-MARS may increase overhead compared with a conventional UAV system
- The overhead should be justified only if mission success and resilience improve
- The paper should avoid claiming zero overhead
- The tradeoff between resilience and resource consumption should be clearly explained

## Mission Recovery Time

This subsection will compare how quickly each system restores stable mission operation after attack detection.

Metrics to include:

- Average recovery time
- Recovery time under jamming
- Recovery time under GPS spoofing
- Recovery time under combined attacks

Expected discussion points:

- Detection alone may not reduce recovery time
- Adaptive mission-continuation logic should reduce recovery delay
- RA-MARS should be evaluated based on operational recovery, not just classification accuracy

## Ablation Study

The ablation study will evaluate the contribution of each RA-MARS module.

Variants to test:

- Full RA-MARS
- RA-MARS without AI detection
- RA-MARS without mission-risk scoring
- RA-MARS without adaptive mission logic
- RA-MARS without tamper-resistant logging

Expected discussion points:

- Which module contributes most to mission success
- Whether adaptive logic improves mission continuity
- Whether tamper-resistant logging improves data trustworthiness
- Whether mission-risk scoring improves decision quality
- Whether all modules are necessary for the full framework

## Defence Relevance

This subsection should connect the results to defence applications.

Discussion should mention:

- Border monitoring
- Battlefield reconnaissance
- Critical-infrastructure protection
- Convoy or perimeter surveillance
- Contested electromagnetic environments
- Need for mission continuity and trustworthy surveillance records

The discussion should be careful and simulation-based. Avoid claiming direct military deployment readiness unless real-world testing is performed.

## Safe Result Language

Use careful language such as:

- Simulation results indicate that...
- Under the tested conditions...
- Compared with the selected baselines...
- The proposed framework shows improved resilience in the simulated scenarios...
- The findings suggest that integrated mission assurance can improve UAV surveillance reliability...
- Further field validation is required before operational deployment.

## Claims to Avoid

Do not write these unless fully supported by strong evidence:

- RA-MARS guarantees secure UAV operation
- RA-MARS is military-grade
- RA-MARS prevents all attacks
- RA-MARS is ready for battlefield deployment
- RA-MARS proves real-world superiority
- RA-MARS has no overhead

## Summary

The results and discussion section should demonstrate that RA-MARS improves multi-UAV mission assurance by connecting attack detection, mission-risk scoring, adaptive mission continuation, and tamper-resistant logging. The main focus should be on measurable operational resilience rather than only AI classification performance.
