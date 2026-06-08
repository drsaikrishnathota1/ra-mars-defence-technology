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
- Full RA-MARS Mission Assurance Index: 0.7497
- Full RA-MARS mission success rate: 85.70%
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
