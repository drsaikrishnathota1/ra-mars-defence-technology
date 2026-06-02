# Cover Letter Draft

Dear Editor-in-Chief,

I am pleased to submit the manuscript entitled “RA-MARS: A Cross-Layer Mission Assurance Digital Twin for Secure Multi-UAV Defence Surveillance Under Cyber-Electromagnetic and Navigation Attacks” for consideration in Defence Technology.

This manuscript proposes RA-MARS, a defence-oriented mission assurance digital twin for secure multi-UAV surveillance in contested environments. The framework integrates temporal AI-based attack detection, a Mission Assurance Index, digital twin-based action selection, adaptive mission continuation, and tamper-resistant mission provenance to address radio-frequency jamming, GPS/GNSS spoofing, mission-data tampering, and combined attacks.

A simulation-based v3 evaluation was conducted using synthetic multi-UAV telemetry data. The optimized dataset contains 90,000 sequence-safe telemetry rows and 16,875 time-series windows, with 20 telemetry steps per window and 9 raw non-leakage features per step. The classifier excludes derived Mission Assurance Index and component scores from attack-detection inputs to avoid feature leakage. Across eight mission-state classes, the best macro-F1 model, Weighted LSTM, achieved 75.25% accuracy, 58.10% macro precision, 60.91% macro recall, 57.02% macro F1-score, and 74.83% weighted F1-score.

The mission-level evaluation shows that full RA-MARS achieved a Mission Assurance Index of 0.7291 ± 0.0057 and a mission success rate of 78.25 ± 0.46% under stressed attack scenarios. Ablation analysis showed that removing adaptive continuation reduced mission success to 61.82%, removing the Mission Assurance Index reduced it to 65.73%, and removing digital twin action selection reduced it to 66.51%. These findings support the value of linking temporal attack detection with mission-level assurance scoring, adaptive operational decisions, and trustworthy mission provenance.

The manuscript aligns with the scope of Defence Technology because it addresses secure and resilient autonomous surveillance systems for defence-relevant contested environments using simulation-based evaluation and mission-level performance metrics. The work contributes to defence science and engineering by connecting cyber-electromagnetic attack detection, mission-risk assessment, adaptive mission continuity, and tamper-resistant logging in a unified multi-UAV mission assurance framework.

This manuscript has not been published previously and is not under consideration for publication elsewhere. The author declares no competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

Thank you for considering this manuscript for publication in Defence Technology.

Kind regards,

Dr. Sai Krishna Thota
