# Leakage Prevention and Reproducibility Controls

To improve scientific validity, the v3 attack-detection experiment uses only raw non-leakage input features. Derived Mission Assurance Index values and derived component scores are excluded from classifier input. The purpose of this design choice is to prevent the model from learning labels indirectly from post-processed risk or assurance scores.

The v3 classifier input includes only the following raw telemetry, communication, navigation, energy, and mission-progress features:

- packet loss rate
- communication latency
- route deviation
- GPS jump
- velocity inconsistency
- battery level
- mission progress
- zone coverage
- energy consumption

The following derived features are not used as classifier inputs:

- Mission Assurance Index
- communication score
- navigation score
- coverage score
- integrity score
- recovery score
- risk level
- adaptive action
- projected mission assurance

The Mission Assurance Index is used only for mission-level evaluation and digital twin decision analysis, not for attack classification. This separation ensures that the attack-detection task remains more realistic and avoids artificial performance inflation.

The v3 dataset uses sequence-safe sampling, where complete UAV time-series groups are preserved before creating 20-step telemetry windows. This prevents broken or randomly scattered windows and supports temporal attack-detection analysis. Fixed random seeds are used for reproducibility. The train/test split is stratified by class labels to preserve class distribution across model evaluation.

All v3 results are based on synthetic simulation data and should be interpreted as simulation-based evidence. The results do not represent real military UAV flight validation, classified operational data, or deployed battlefield testing.
