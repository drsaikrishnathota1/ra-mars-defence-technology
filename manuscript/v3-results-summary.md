# RA-MARS v3 Results Summary

## Purpose

This file summarizes the optimized RA-MARS v3 results for manuscript integration. The v3 evaluation improves over v2 by using time-series telemetry windows, non-leakage raw features, class-aware sequence modeling, ablation analysis, mission assurance evaluation, scalability testing, and attack-intensity stress testing.

## Dataset Configuration

The optimized v3 dataset was generated using a fast RunPod-safe configuration. The full intermediate dataset was not saved to avoid excessive storage. Only a sequence-safe sample was saved.

Key dataset properties:

- Sample file: `simulations/datasets/uav_mission_telemetry_v3_sample.csv`
- Sample size: 90,000 telemetry rows
- Sequence file: `simulations/datasets/uav_sequence_windows_v3.npz`
- Sequence windows: 16,875
- Window size: 20 telemetry steps
- Input features per time step: 9
- Attack classes: 8

The classifier input uses only non-leakage raw telemetry, communication, navigation, energy, and mission-progress features. Derived Mission Assurance Index and component scores are excluded from classifier input.

## Sequence Label Distribution

See:

`simulations/datasets/sequence_label_distribution_v3.csv`

The v3 sequence dataset contains the following classes:

- normal
- jamming
- spoofing
- tampering
- jamming_spoofing
- jamming_tampering
- spoofing_tampering
- combined

## Model Results

The v3 model evaluation includes classical sequence baselines, unweighted GRU/LSTM models, and weighted GRU/LSTM models.

Important result files:

- `simulations/results/model_performance_v3_classical.csv`
- `simulations/results/model_performance_v3_sequence.csv`
- `simulations/results/model_performance_v3_sequence_weighted.csv`
- `simulations/results/model_performance_v3_combined_summary.csv`
- `simulations/results/per_class_metrics_v3_classical.csv`
- `simulations/results/per_class_metrics_v3_sequence_weighted.csv`
- `simulations/results/confusion_matrix_v3_classical.csv`
- `simulations/results/confusion_matrix_v3_sequence_weighted.csv`

## Key Interpretation

The optimized v3 results are more realistic than v2 because the classifier uses temporal windows and excludes derived risk or mission-assurance scores from the feature set.

The results show that non-leakage sequence-based attack classification is more difficult than the earlier v2 experiments, but it is more scientifically defensible. The weighted sequence model improves minority-class treatment compared with the unweighted sequence model, while Random Forest remains a strong classical baseline.

## Mission Assurance and Ablation Results

The v3 mission-level analysis adds:

- Mission Assurance Index
- ablation study
- detection delay analysis
- scalability analysis
- attack-intensity stress testing

Important result files:

- `simulations/results/ablation_results_v3.csv`
- `simulations/results/mission_assurance_index_v3.csv`
- `simulations/results/detection_delay_v3.csv`
- `simulations/results/scalability_results_v3.csv`
- `simulations/results/attack_intensity_results_v3.csv`

The ablation study compares:

- Full RA-MARS
- Without AI Detection
- Without Mission Assurance Index
- Without Adaptive Continuation
- Without Digital Twin Action Selection
- Without Tamper-Resistant Logging
- Without Navigation Trust Module

## v3 Journal Figures

The v3 journal-grade figures are stored in:

`figures/graphs/v3/`

Expected figures include:

- model comparison by macro F1
- model comparison by accuracy
- per-class F1-score
- confusion matrix
- sequence class distribution
- ablation mission success
- ablation Mission Assurance Index
- mission assurance by scenario
- scalability mission success
- attack-intensity stress test

## Manuscript Integration Notes

The v3 manuscript should emphasize the following improvements over v2:

1. RA-MARS is repositioned as a cross-layer mission assurance digital twin.
2. Attack detection is performed using temporal sequence windows rather than isolated rows.
3. Only raw non-leakage features are used for classifier input.
4. The Mission Assurance Index is used as a mission-level evaluation metric, not as an attack-classifier input.
5. Ablation results show the contribution of each RA-MARS module.
6. Scalability and attack-intensity stress tests make the evaluation more defence-relevant.
7. The results are realistic and should not be overclaimed as real-world UAV validation.

## Research Integrity Statement

The v3 results are based on synthetic simulation data. They do not represent real military UAV flight data, classified operational data, or field-tested deployment. The results should be described as simulation-based evidence supporting the feasibility of a mission-assurance digital twin for multi-UAV defence surveillance under cyber-electromagnetic and navigation attacks.
