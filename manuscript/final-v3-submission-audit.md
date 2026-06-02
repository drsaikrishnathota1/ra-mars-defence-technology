# RA-MARS Final v3 Submission Audit

## Final Submission Manuscript

Use only:

- `manuscript/RA-MARS-journal-draft-final-v3.md`
- `manuscript/RA-MARS-journal-draft-final-v3.docx`

Do not submit legacy v2 drafts.

## Final Title

RA-MARS: A Cross-Layer Mission Assurance Digital Twin for Secure Multi-UAV Defence Surveillance Under Cyber-Electromagnetic and Navigation Attacks

## Final v3 Dataset Summary

- Synthetic simulation data only
- 90,000 sequence-safe telemetry rows
- 16,875 time-series windows
- 20 telemetry steps per window
- 9 raw non-leakage features per step
- 8 mission-state classes

## Final v3 Model Results

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

## Final v3 Mission Assurance Results

Full RA-MARS:

- Mission Assurance Index: 0.7291 ± 0.0057
- Mission Success Rate: 78.25 ± 0.46%
- Packet Delivery Ratio: 0.9533
- Route Deviation: 36.88 m
- Recovery Time Proxy: 5.81 s

Ablation:

- Without Adaptive Continuation: 61.82% mission success
- Without Mission Assurance Index: 65.73% mission success
- Without Digital Twin Action Selection: 66.51% mission success
- Without Navigation Trust Module: 64.17% mission success

Scalability:

- 10 UAVs: 80.19 ± 0.63%
- 20 UAVs: 79.42 ± 0.54%
- 30 UAVs: 79.38 ± 0.52%

Attack intensity:

- Low: 81.34 ± 0.17%
- Medium: 79.70 ± 0.36%
- High: 76.98 ± 0.62%

## Final Figure Sets

Conceptual figures:

- Cross-layer architecture
- Threat model
- Closed-loop workflow
- Mission Assurance Index components
- Experimental pipeline
- Attack timeline
- Digital twin action selection

Result figures:

- Model comparison by macro F1
- Model comparison by accuracy
- Per-class F1
- Confusion matrix
- Sequence class distribution
- Ablation mission success
- Ablation Mission Assurance Index
- Mission assurance by scenario
- Scalability mission success
- Attack intensity stress test

## Research Integrity Controls

- v3 classifier uses raw non-leakage features only.
- Mission Assurance Index is not used as classifier input.
- Derived component scores are not used as classifier input.
- Synthetic data limitation is stated.
- No real military deployment claim is made.
- No real UAV flight validation claim is made.
- No battlefield-ready or military-grade claim should be made.

## Remaining Before Submission

- Verify all references and DOI values.
- Convert references to exact Defence Technology / Elsevier style.
- Run grammar check.
- Run similarity/plagiarism check.
- Visually inspect final Word document.
- Confirm all figures are readable.
- Confirm all tables fit Word page width.
- Confirm final title matches cover letter and highlights.
