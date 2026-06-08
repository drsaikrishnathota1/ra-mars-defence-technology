# RA-MARS: Resilient AI-Driven Mission Assurance for Secure Multi-UAV Defence Surveillance

## Working Title
RA-MARS: A Resilient AI-Driven Mission Assurance Framework for Secure Multi-UAV Defence Surveillance Under Jamming, GPS Spoofing, and Data-Tampering Attacks

## Target Journal
Defence Technology

## Project Goal
This repository documents the development of a defence-oriented journal article focused on secure and resilient multi-UAV surveillance in contested environments.

## Proposed Framework
RA-MARS integrates:
- AI-based attack detection
- Mission-risk scoring
- Adaptive mission-continuation logic
- Blockchain-inspired tamper-resistant mission logging
- Simulation-based performance evaluation

## Main Threats
- RF jamming
- GPS/GNSS spoofing
- Mission-data tampering
- Combined attack scenarios

## Main Evaluation Metrics
- Mission success rate
- Attack detection accuracy
- Precision
- Recall
- F1-score
- Packet delivery ratio
- Average latency
- Energy consumption
- Tamper-detection rate
- Mission recovery time

## Repository Structure
- literature-review: references, literature matrix, and notes
- manuscript: article section drafts and final paper plan
- simulations: Python/NS-3 simulation files, datasets, and results
- figures: architecture, threat model, and result graph plans
- tables: simulation parameters, baseline comparison, and result summaries
- submission: cover letter, highlights, declaration, and response notes
- archive: older drafts and unused material

## Current Status

RA-MARS v4 simulation pipeline has been completed on RunPod. The repository now includes a physics-based RF/SINR dataset workflow, sequence-window generation, binary and fine-grained LSTM/GRU models, classical baselines, mission-assurance evaluation, ablation analysis, scalability testing, attack-intensity testing, latency-budget analysis, and adversarial training results.

## Key v4 Results

- Binary GRU attack-vs-normal classification: macro-F1 = 0.9577, accuracy = 0.9577
- Binary LSTM attack-vs-normal classification: macro-F1 = 0.9573, accuracy = 0.9573
- Fine-grained Weighted GRU 8-class classification: macro-F1 = 0.6007, accuracy = 0.7536
- Full RA-MARS Mission Assurance Index: 0.7012
- Full RA-MARS mission success rate: 73.61%
- Framework overhead: 11.5 ms per telemetry cycle
- Adversarially trained binary LSTM clean macro-F1: 0.9986
- FGSM ε=0.01 macro-F1 after adversarial training: 0.9975
- PGD ε=0.05 macro-F1 after adversarial training: 0.9831

## Next Phase

1. Update the manuscript from v3 results to v4 results.
2. Create paper-ready result tables and figures from the generated CSV files.
3. Move selected final CSVs into a lightweight reproducibility folder.
4. Polish the methodology, results, limitations, and conclusion sections.
5. Prepare the final Defence Technology submission package.

## Research Integrity Notes
This project uses simulation-generated synthetic UAV telemetry data. It should not be presented as real military flight data.

All final numerical results must be generated from simulation scripts and saved in CSV files before being used in the manuscript.

RA-MARS should be positioned as a defence mission-assurance framework, not as a generic AI, blockchain, or quantum paper.

# RA-MARS v5 Completed Validation Status

Updated: 2026-06-08 06:29
Branch: `main`
Latest commit: `04f9546`

## Current Status

The RA-MARS repository now contains completed v5 validation outputs and updated manuscript/submission files.

Completed items:

- Active v3 references removed from v4/v5 training workflow.
- Sequence windows now store raw unscaled telemetry windows.
- LSTM/GRU sequence models use train-only feature standardization.
- Classical baselines use train-only feature standardization.
- 1D-CNN temporal baseline added and evaluated.
- Clean 9-step RunPod pipeline created.
- Completed v5 result CSVs copied into `simulations/final-results/`.
- Paper-ready v5 result tables generated in `tables/final-v5/`.
- Manuscript updated with completed v5 validation values.
- Cover letter and highlights updated with completed v5 values.
- Synthetic-data and controlled-telemetry limitation is explicitly stated.

## Completed v5 Headline Results

- Binary LSTM: 99.85% accuracy, 99.81% macro-F1.
- Binary GRU: 99.80% accuracy, 99.76% macro-F1.
- Weighted LSTM fine-grained: 99.53% accuracy, 99.18% macro-F1.
- Weighted GRU fine-grained: 99.24% accuracy, 98.66% macro-F1.
- 1D-CNN binary baseline: 99.97% accuracy, 99.96% macro-F1.
- 1D-CNN fine-grained baseline: 98.82% accuracy, 98.18% macro-F1.
- Full RA-MARS Mission Assurance Index: 0.7012.
- Full RA-MARS mission success rate: 73.61%.
- Framework overhead: 11.5 ms per telemetry cycle.

## Important Interpretation

The high classification scores are interpreted within a controlled synthetic-telemetry setting. The data are simulation-generated and physics-informed, but they are not real military flight-test data, classified operational data, hardware-in-the-loop results, or deployed battlefield validation.

The main contribution of RA-MARS is the mission-assurance integration of attack detection, mission-risk scoring, adaptive mission continuation, and tamper-evident mission provenance.

## Key Current Files

- `manuscript/RA-MARS-journal-draft-final-v4.md`
- `tables/final-v5/ra_mars_v5_completed_result_tables.md`
- `simulations/final-results/`
- `submission/cover-letter.md`
- `submission/highlights.md`
- `submission/declaration-of-interest.md`
- `simulations/python/runpod_run_all.sh`

## Recent Commits

```text
04f9546 (HEAD -> main, origin/main, origin/HEAD) Update README with completed v5 validation status
0ce8f41 Update README with completed v5 validation status
54742ba Update submission files with completed v5 results
e9789ab Update manuscript with completed v5 validation results
6aea1d1 Add v5 completed result tables
3b7f55b Update raw v5 validation result artifacts
28fe82a Update final results with completed v5 validation outputs
e63ddc6 Apply train-only scaling inside sequence model training
4b4e6db Clean RunPod pipeline with single 1D-CNN baseline step
dbdfc0d Clean RunPod pipeline with single 1D-CNN baseline step
b5f434a Add 1D-CNN baseline to RunPod pipeline
a071c72 Add 1D-CNN baseline to RunPod pipeline
```

## Remaining Before Submission

1. Regenerate final figures from v5 result CSVs.
2. Refresh final submission package folder.
3. Export updated DOCX/HTML.
4. Prepare anonymized manuscript version for double-anonymized review.
5. Do final formatting and reference check.
