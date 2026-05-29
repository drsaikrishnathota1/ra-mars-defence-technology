# RA-MARS Final Paper Assembly Plan

## Target Journal
Defence Technology

## Working Title
RA-MARS: A Resilient AI-Driven Mission Assurance Framework for Secure Multi-UAV Defence Surveillance Under Jamming, GPS Spoofing, and Data-Tampering Attacks

## Purpose
This file explains how the individual manuscript sections will be assembled into the final journal paper.

## Final Manuscript Structure

### 1. Title Page
Include:
- Full manuscript title
- Author name
- Affiliation
- Corresponding author email
- Keywords
- Highlights
- Declaration of competing interest

### 2. Abstract
Source file:
`manuscript/abstract.md`

The final abstract should be revised after simulation results are available.

### 3. Keywords
Recommended keywords:
- Multi-UAV systems
- Defence surveillance
- Mission assurance
- UAV cybersecurity
- Jamming detection
- GPS spoofing
- Data tampering
- Artificial intelligence
- Tamper-resistant logging
- Contested environments

### 4. Introduction
Source file:
`manuscript/introduction.md`

The introduction should include:
- Defence motivation
- Problem statement
- Research gap
- Proposed solution
- Contributions
- Paper organization

### 5. Related Work
Source file:
`manuscript/related-work.md`

This section must be expanded after collecting 45–70 references.

Required subsections:
- UAV defence surveillance and reconnaissance
- Multi-UAV mission planning and mission assurance
- RF jamming detection and anti-jamming
- GPS/GNSS spoofing detection
- AI-based anomaly detection
- UAV cybersecurity
- Tamper-resistant mission logging
- Research gap summary

### 6. System Model and Threat Model
New section to write later.

Should include:
- Multi-UAV mission environment
- Ground control station
- Communication model
- Mission-zone model
- RF jamming attack
- GPS spoofing attack
- Data-tampering attack
- Combined attack scenario
- Assumptions and limitations

### 7. Proposed RA-MARS Framework
Source file:
`manuscript/methodology.md`

Should include:
- System architecture
- AI-based attack detection
- Mission-risk scoring
- Adaptive mission-continuation logic
- Tamper-resistant mission logging
- RA-MARS workflow
- Algorithm/pseudocode

### 8. Experimental Setup
New section to write after simulation code is prepared.

Should include:
- Simulation environment
- Dataset generation
- UAV mission scenario
- Attack injection settings
- Baseline methods
- Evaluation metrics

### 9. Results and Discussion
Source file:
`manuscript/results-discussion.md`

Will be completed after simulation results are generated.

Required results:
- AI model performance
- Mission success rate
- Communication performance
- GPS spoofing detection / route deviation
- Tamper-detection performance
- Energy and latency overhead
- Mission recovery time
- Ablation study

### 10. Limitations
Include:
- Simulation-generated dataset
- No real UAV flight testing
- No real military field validation
- Simplified attack models
- Lightweight blockchain-inspired logging only
- Future validation required

### 11. Conclusion
Source file:
`manuscript/conclusion.md`

The conclusion should be revised after final results are available.

### 12. References
Source files:
- `literature-review/reference-list.md`
- `literature-review/literature-matrix.md`

Final target:
- 45–70 references
- At least 25 references from 2021–2026

## Required Figures

| Figure | Source Planning File | Status |
|---|---|---|
| Figure 1: RA-MARS architecture | figures/architecture/ra-mars-architecture.md | Planned |
| Figure 2: Threat model | figures/threat-model/threat-model.md | Planned |
| Figure 3: AI detection workflow | TBD | Not started |
| Figure 4: Mission-risk decision flow | TBD | Not started |
| Figure 5: Tamper-resistant logging process | TBD | Not started |
| Figure 6: Simulation environment | TBD | Not started |
| Figure 7: Results graphs | figures/graphs/graph-plan.md | Planned |
| Figure 8: Ablation study | figures/graphs/graph-plan.md | Planned |

## Required Tables

| Table | Source File | Status |
|---|---|---|
| Table 1: Related-work comparison | literature-review/literature-matrix.md | Template created |
| Table 2: Threat model | figures/threat-model/threat-model.md | Planned |
| Table 3: Simulation parameters | tables/simulation-parameters.md | Planned |
| Table 4: Baseline comparison | tables/baseline-comparison.md | Planned |
| Table 5: Results summary | tables/results-summary.md | Planned |
| Table 6: Ablation study | tables/results-summary.md | Planned |

## Final Submission Package

Required files:
- Final manuscript
- Cover letter
- Highlights
- Declaration of competing interest
- Figures
- Tables
- References
- Data availability statement
- Code availability statement, if applicable

## Submission Readiness Checklist

- [ ] Title is finalized
- [ ] Abstract includes final results
- [ ] Introduction clearly states novelty
- [ ] Related work includes 45–70 references
- [ ] Research gap is clearly stated
- [ ] Contributions are specific and measurable
- [ ] Methodology is technically detailed
- [ ] Simulation code is completed
- [ ] Results are generated from code
- [ ] Figures are publication quality
- [ ] Tables are complete
- [ ] Limitations are honestly stated
- [ ] Cover letter is polished
- [ ] Similarity check completed
- [ ] All citations are verified
- [ ] Journal formatting checked

## Important Reminder
The final paper should not be submitted until simulation results, verified references, and novelty comparison are complete.
