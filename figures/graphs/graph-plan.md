# RA-MARS Result Graph Plan

## Purpose
This file defines the planned graphs for the RA-MARS manuscript. The goal is to ensure that the results section has clear, publication-quality visual evidence.

## Target Journal
Defence Technology

## Study Title
RA-MARS: A Resilient AI-Driven Mission Assurance Framework for Secure Multi-UAV Defence Surveillance Under Jamming, GPS Spoofing, and Data-Tampering Attacks

## Important Note
Do not create final result graphs manually. Final graphs must be generated from simulation result CSV files.

## Planned Graphs

## Graph 1: AI Attack Detection Performance

### Purpose
Compare machine-learning models for attack classification.

### Graph Type
Grouped bar chart.

### X-Axis
AI models:
- Logistic Regression
- Support Vector Machine
- Random Forest
- Gradient Boosting / XGBoost
- Lightweight Neural Network

### Y-Axis
Score percentage.

### Metrics
- Accuracy
- Precision
- Recall
- F1-score

### Source File
`simulations/results/model_performance.csv`

### Manuscript Use
This graph will support selection of the AI detection model used in RA-MARS.

---

## Graph 2: Mission Success Rate Across Attack Scenarios

### Purpose
Show whether RA-MARS improves mission completion under normal and adversarial conditions.

### Graph Type
Grouped bar chart.

### X-Axis
Attack scenarios:
- Normal
- Jamming
- GPS spoofing
- Data tampering
- Combined attack

### Y-Axis
Mission success rate percentage.

### Methods Compared
- Conventional UAV system
- AI-only detection
- Logging-only system
- Non-adaptive secure system
- RA-MARS

### Source File
`simulations/results/mission_success_results.csv`

### Manuscript Use
This is one of the most important graphs because Defence Technology will care about mission-level impact.

---

## Graph 3: Packet Delivery Ratio Under Jamming

### Purpose
Evaluate communication reliability under jamming intensity.

### Graph Type
Line chart or grouped bar chart.

### X-Axis
Jamming intensity:
- None
- Low
- Medium
- High

### Y-Axis
Packet delivery ratio.

### Methods Compared
- Conventional UAV system
- AI-only detection
- Non-adaptive secure system
- RA-MARS

### Source File
`simulations/results/communication_results.csv`

### Manuscript Use
This graph supports the communication-resilience claim.

---

## Graph 4: Average Latency Under Attack

### Purpose
Compare communication delay and security overhead across methods.

### Graph Type
Bar chart.

### X-Axis
Methods:
- Conventional UAV system
- AI-only detection
- Logging-only system
- Non-adaptive secure system
- RA-MARS

### Y-Axis
Average latency in milliseconds.

### Source File
`simulations/results/communication_results.csv`

### Manuscript Use
This graph shows whether RA-MARS adds acceptable overhead.

---

## Graph 5: GPS Spoofing Detection and Route Deviation

### Purpose
Show how the framework detects spoofing and controls route deviation.

### Graph Type
Line chart or bar chart.

### X-Axis
Spoofing severity:
- None
- Low
- Medium
- High

### Y-Axis
Average route deviation in meters.

### Methods Compared
- Conventional UAV system
- AI-only detection
- Non-adaptive secure system
- RA-MARS

### Source File
`simulations/results/navigation_results.csv`

### Manuscript Use
This graph supports navigation-trustworthiness discussion.

---

## Graph 6: Tamper-Detection Rate

### Purpose
Compare mission-log integrity protection.

### Graph Type
Bar chart.

### X-Axis
Logging methods:
- Conventional logs
- Hash-chain logging
- Blockchain-inspired logging
- RA-MARS logging module

### Y-Axis
Tamper-detection rate percentage.

### Source File
`simulations/results/tamper_detection_results.csv`

### Manuscript Use
This graph supports mission-data trustworthiness.

---

## Graph 7: Energy Consumption and Operational Overhead

### Purpose
Show the tradeoff between resilience and resource usage.

### Graph Type
Grouped bar chart.

### X-Axis
Methods:
- Conventional UAV system
- AI-only detection
- Logging-only system
- Non-adaptive secure system
- RA-MARS

### Y-Axis
Energy consumption or battery usage percentage.

### Source File
`simulations/results/energy_results.csv`

### Manuscript Use
This graph supports overhead discussion.

---

## Graph 8: Mission Recovery Time

### Purpose
Show how quickly the system restores stable mission operation after attack detection.

### Graph Type
Bar chart.

### X-Axis
Attack scenarios:
- Jamming
- GPS spoofing
- Data tampering
- Combined attack

### Y-Axis
Mission recovery time in seconds.

### Methods Compared
- AI-only detection
- Non-adaptive secure system
- RA-MARS

### Source File
`simulations/results/recovery_time_results.csv`

### Manuscript Use
This graph supports mission-continuity and adaptive-response claims.

---

## Graph 9: Ablation Study

### Purpose
Show the contribution of each RA-MARS module.

### Graph Type
Bar chart.

### X-Axis
RA-MARS variants:
- Full RA-MARS
- Without AI detection
- Without risk scoring
- Without adaptive logic
- Without tamper-resistant logging

### Y-Axis
Mission success rate or resilience score.

### Source File
`simulations/results/ablation_results.csv`

### Manuscript Use
This graph helps prove novelty and module contribution.

---

## Graph 10: Risk Score Distribution

### Purpose
Show how RA-MARS assigns risk scores under different mission states.

### Graph Type
Box plot or histogram.

### X-Axis
Mission state:
- Normal
- Jamming
- Spoofing
- Tampering
- Combined

### Y-Axis
Risk score.

### Source File
`simulations/results/risk_score_results.csv`

### Manuscript Use
This graph supports mission-risk scoring validation.

---

## Graph Quality Guidelines

Final graphs should be:

- Clear
- High resolution
- Publication style
- Properly labeled
- Easy to read in grayscale
- Generated from CSV files
- Saved as PNG and PDF where possible

## Suggested Output Folder

Save final graphs in:

`figures/graphs/final/`

Suggested filenames:

- `graph1_ai_detection_performance.png`
- `graph2_mission_success_rate.png`
- `graph3_packet_delivery_ratio.png`
- `graph4_average_latency.png`
- `graph5_route_deviation.png`
- `graph6_tamper_detection_rate.png`
- `graph7_energy_consumption.png`
- `graph8_mission_recovery_time.png`
- `graph9_ablation_study.png`
- `graph10_risk_score_distribution.png`

## Manuscript Reminder

The final manuscript should not include too many graphs if space is limited. Prioritize:

1. Mission success rate
2. Attack detection performance
3. Packet delivery ratio
4. Tamper-detection rate
5. Ablation study
6. Energy/latency overhead
