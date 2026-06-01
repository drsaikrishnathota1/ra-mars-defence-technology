# RA-MARS v3 Enhancement Plan

## Purpose

RA-MARS v3 upgrades the current framework into a cross-layer mission assurance digital twin for secure multi-UAV defence surveillance under cyber-electromagnetic and navigation attacks.

## New Positioning

RA-MARS v3 is positioned as:

A cross-layer mission assurance digital twin for secure multi-UAV defence surveillance under cyber-electromagnetic and navigation warfare.

## Core v3 Additions

- Time-series telemetry windows
- Adaptive jamming, spoofing, and tampering attacks
- Mission Assurance Index
- Digital twin action selection
- Temporal AI models
- Ablation study
- Confidence intervals over multiple seeds
- Detection delay analysis
- Scalability analysis
- Journal-grade figures

## Final v3 Claim

RA-MARS v3 converts cyber-electromagnetic attack indicators into mission-level assurance decisions by linking temporal attack detection, mission assurance scoring, adaptive continuation, and tamper-resistant mission provenance.

## v3 Research Contributions

1. Cross-layer threat model for jamming, GPS/GNSS spoofing, data tampering, and combined attacks.
2. Temporal AI attack detection using UAV telemetry windows.
3. Mission Assurance Index combining communication, navigation, coverage, integrity, recovery, and energy indicators.
4. Digital twin-based adaptive mission continuation that compares candidate actions.
5. Tamper-resistant mission provenance for post-mission trust.
6. Comprehensive evaluation using ablation, confidence intervals, detection delay, scalability, and attack-intensity testing.

## v3 Simulation Enhancements

### RF Jamming Types

- barrage jamming
- intermittent jamming
- reactive jamming
- adaptive jamming

### GPS/GNSS Spoofing Types

- sudden jump spoofing
- gradual drift spoofing
- coordinated swarm spoofing

### Mission-Data Tampering Types

- position tampering
- timestamp tampering
- mission-progress tampering
- selective log tampering

### Combined Attacks

- jamming + spoofing
- spoofing + tampering
- jamming + tampering
- jamming + spoofing + tampering

## Attack Intensities

- low
- medium
- high

## Swarm Sizes

- 10 UAVs
- 20 UAVs
- 30 UAVs
- 50 UAVs

## Simulation Seeds

Use multiple random seeds to support confidence intervals.

## v3 Models

Classical models:
- Random Forest
- Gradient Boosting
- XGBoost
- LightGBM

Deep/time-series models:
- MLP
- GRU
- LSTM
- Temporal CNN
- Transformer Encoder

## v3 Metrics

Attack detection:
- accuracy
- precision
- recall
- F1-score
- per-class precision
- per-class recall
- per-class F1
- confusion matrix
- detection delay
- false alarm rate

Mission assurance:
- mission success rate
- Mission Assurance Index
- packet delivery ratio
- average latency
- route deviation
- zone coverage
- tamper-detection rate
- energy consumption
- mission recovery time

Statistical reporting:
- mean
- standard deviation
- 95% confidence interval

## v3 Ablation Study

Compare:

- Full RA-MARS
- Without AI detection
- Without Mission Assurance Index
- Without adaptive continuation
- Without digital twin action selection
- Without tamper-resistant logging
- Without navigation trust module

## v3 Figures

Required figures:

1. RA-MARS v3 cross-layer architecture
2. Cyber-electromagnetic threat model
3. Closed-loop digital twin workflow
4. Attack timeline with detection/recovery
5. Mission Assurance Index components
6. Confusion matrix
7. Per-class F1-score
8. Ablation study
9. Mission success with 95% confidence intervals
10. Recovery time with 95% confidence intervals
11. Scalability: UAV count vs mission success
12. Attack intensity stress test

## v3 Output Files

Scripts:
- simulations/python/generate_dataset_v3.py
- simulations/python/create_sequence_windows_v3.py
- simulations/python/train_classical_models_v3.py
- simulations/python/train_sequence_models_v3.py
- simulations/python/evaluate_ablation_v3.py
- simulations/python/evaluate_confidence_intervals_v3.py
- simulations/python/generate_journal_figures_v3.py
- simulations/python/compute_mission_assurance_index_v3.py

Results:
- simulations/results/model_performance_v3.csv
- simulations/results/per_class_metrics_v3.csv
- simulations/results/confusion_matrix_v3.csv
- simulations/results/ablation_results_v3.csv
- simulations/results/mission_success_ci_v3.csv
- simulations/results/recovery_time_ci_v3.csv
- simulations/results/mission_assurance_index_v3.csv
- simulations/results/detection_delay_v3.csv
- simulations/results/scalability_results_v3.csv
- simulations/results/attack_intensity_results_v3.csv

## Submission Strategy

Use v3 results for the final manuscript.

Keep v2 as development history, but use v3 as the final journal result set if completed successfully.
