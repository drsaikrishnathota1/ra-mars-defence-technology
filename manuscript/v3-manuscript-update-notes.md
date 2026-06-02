# RA-MARS v3 Manuscript Update Notes

## New Positioning

RA-MARS is updated from a general AI-driven mission assurance framework into a cross-layer mission assurance digital twin for secure multi-UAV defence surveillance under cyber-electromagnetic and navigation attacks.

## v3 Dataset

The optimized v3 evaluation uses:

- 90,000 sequence-safe telemetry rows
- 16,875 time-series windows
- 20 telemetry steps per window
- 9 raw non-leakage features per step
- 8 classes: normal, jamming, spoofing, tampering, jamming_spoofing, jamming_tampering, spoofing_tampering, and combined

The classifier excludes derived Mission Assurance Index and component scores from the attack-detection input features to avoid leakage.

## v3 Model Results

Best macro-F1 model:

- Weighted LSTM
- Accuracy: 75.25%
- Macro Precision: 58.10%
- Macro Recall: 60.91%
- Macro F1-score: 57.02%
- Weighted F1-score: 74.83%

Best accuracy model:

- LSTM
- Accuracy: 78.24%
- Macro F1-score: 53.40%
- Weighted F1-score: 73.84%

Best classical baseline:

- Random Forest
- Accuracy: 77.06%
- Macro F1-score: 56.56%
- Weighted F1-score: 74.72%

## Mission Assurance Results

Full RA-MARS:

- Mission Assurance Index: 0.7291 ± 0.0057
- Mission Success Rate: 78.25 ± 0.46%
- Packet Delivery Ratio: 0.9533
- Route Deviation: 36.88 m
- Recovery Time Proxy: 5.81 s

Ablation results show that removing adaptive continuation reduces mission success to 61.82%, removing the Mission Assurance Index reduces it to 65.73%, and removing digital twin action selection reduces it to 66.51%.

## Scalability Results

Mission success remains stable across swarm sizes:

- 10 UAVs: 80.19 ± 0.63%
- 20 UAVs: 79.42 ± 0.54%
- 30 UAVs: 79.38 ± 0.52%

## Attack Intensity Stress Test

Mission success decreases as attack intensity increases:

- Low intensity: 81.34 ± 0.17%
- Medium intensity: 79.70 ± 0.36%
- High intensity: 76.98 ± 0.62%

## Manuscript Claim

The v3 results support the claim that RA-MARS improves multi-UAV mission assurance by linking temporal attack detection, Mission Assurance Index scoring, digital twin-based action selection, adaptive mission continuation, and tamper-resistant mission provenance.

## Important Integrity Note

The v3 results are based on synthetic simulation data. The manuscript must not claim real-world military UAV deployment or real flight validation.
