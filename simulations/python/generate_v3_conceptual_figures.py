"""
RA-MARS v3 Conceptual Journal Figure Generator

Creates additional journal-grade conceptual diagrams:
- Cross-layer digital twin architecture
- Closed-loop workflow
- Mission Assurance Index components
- Attack timeline
- Digital twin action selection
- v3 experimental pipeline
"""

from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle
import numpy as np


OUT_DIR = Path("figures/conceptual/v3")
OUT_DIR.mkdir(parents=True, exist_ok=True)


def box(ax, x, y, w, h, text, fs=9):
    rect = Rectangle((x, y), w, h, fill=False, linewidth=1.4)
    ax.add_patch(rect)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, wrap=True)


def arrow(ax, x1, y1, x2, y2):
    ax.add_patch(
        FancyArrowPatch(
            (x1, y1),
            (x2, y2),
            arrowstyle="->",
            mutation_scale=13,
            linewidth=1.2,
        )
    )


def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT_DIR / f"{name}.png", dpi=600)
    fig.savefig(OUT_DIR / f"{name}.pdf")
    plt.close(fig)


def cross_layer_architecture():
    fig, ax = plt.subplots(figsize=(13, 7))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 7)
    ax.axis("off")

    ax.set_title("RA-MARS v3 Cross-Layer Mission Assurance Digital Twin", fontsize=14, fontweight="bold")

    box(ax, 0.5, 5.2, 2.1, 0.8, "Multi-UAV\nMission Layer")
    box(ax, 0.5, 4.0, 2.1, 0.8, "Telemetry Layer\nPosition, Battery,\nCoverage")
    box(ax, 0.5, 2.8, 2.1, 0.8, "Communication Layer\nPDR, Loss,\nLatency")
    box(ax, 0.5, 1.6, 2.1, 0.8, "Integrity Layer\nMission Logs,\nHashes")

    box(ax, 3.3, 4.8, 2.1, 0.9, "Temporal AI\nAttack Detection")
    box(ax, 3.3, 3.4, 2.1, 0.9, "Mission Assurance\nIndex")
    box(ax, 3.3, 2.0, 2.1, 0.9, "Risk State\nEstimation")

    box(ax, 6.3, 4.1, 2.2, 1.0, "Digital Twin\nMission Projection")
    box(ax, 6.3, 2.5, 2.2, 1.0, "Candidate Action\nEvaluation")

    box(ax, 9.3, 4.8, 2.3, 0.9, "Adaptive Mission\nContinuation")
    box(ax, 9.3, 3.4, 2.3, 0.9, "Tamper-Resistant\nProvenance")
    box(ax, 9.3, 2.0, 2.3, 0.9, "Mission Assurance\nDecision Output")

    for yy in [5.6, 4.4, 3.2, 2.0]:
        arrow(ax, 2.6, yy, 3.3, 4.2)

    arrow(ax, 5.4, 5.25, 6.3, 4.7)
    arrow(ax, 5.4, 3.85, 6.3, 4.4)
    arrow(ax, 5.4, 2.45, 6.3, 3.0)

    arrow(ax, 8.5, 4.6, 9.3, 5.25)
    arrow(ax, 8.5, 3.0, 9.3, 3.85)
    arrow(ax, 8.5, 3.0, 9.3, 2.45)

    save(fig, "figure_v3_cross_layer_architecture")


def closed_loop_workflow():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis("off")

    ax.set_title("RA-MARS v3 Closed-Loop Mission Assurance Workflow", fontsize=14, fontweight="bold")

    steps = [
        ("Observe\nTelemetry", 0.5),
        ("Detect\nAttack State", 2.4),
        ("Score\nMission Assurance", 4.3),
        ("Predict\nCandidate Outcomes", 6.2),
        ("Select\nAdaptive Action", 8.1),
        ("Log\nMission Provenance", 10.0),
    ]

    for text, x in steps:
        box(ax, x, 3.0, 1.5, 1.0, text, fs=9)

    for i in range(len(steps) - 1):
        arrow(ax, steps[i][1] + 1.5, 3.5, steps[i + 1][1], 3.5)

    arrow(ax, 10.75, 3.0, 1.25, 2.0)
    ax.text(5.8, 1.55, "Closed-loop feedback updates mission state, risk level, and future action selection", ha="center", fontsize=10)

    save(fig, "figure_v3_closed_loop_workflow")


def mai_components():
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis("off")

    ax.set_title("Mission Assurance Index Component Model", fontsize=14, fontweight="bold")

    center = Circle((5, 3.5), 1.0, fill=False, linewidth=1.8)
    ax.add_patch(center)
    ax.text(5, 3.5, "Mission\nAssurance\nIndex", ha="center", va="center", fontsize=10)

    components = [
        ("Communication\nReliability", 1.0, 5.3),
        ("Navigation\nTrustworthiness", 4.0, 5.8),
        ("Coverage\nCompletion", 7.0, 5.3),
        ("Log Integrity\nProvenance", 1.0, 1.2),
        ("Recovery\nEfficiency", 4.0, 0.7),
        ("Energy\nPenalty", 7.0, 1.2),
    ]

    for text, x, y in components:
        box(ax, x, y, 2.0, 0.8, text)
        arrow(ax, x + 1, y + 0.4, 5, 3.5)

    ax.text(
        5,
        6.5,
        "MAI combines mission-level reliability, trust, continuity, and recovery indicators",
        ha="center",
        fontsize=10,
    )

    save(fig, "figure_v3_mission_assurance_index_components")


def attack_timeline():
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.set_xlim(0, 240)
    ax.set_ylim(0, 5)
    ax.set_title("RA-MARS v3 Attack Timeline With Detection and Recovery", fontsize=14, fontweight="bold")

    ax.hlines(4, 0, 240, linewidth=2)
    ax.hlines(3, 0, 240, linewidth=2)
    ax.hlines(2, 0, 240, linewidth=2)
    ax.hlines(1, 0, 240, linewidth=2)

    ax.broken_barh([(60, 120)], (3.8, 0.35), label="Jamming Window")
    ax.broken_barh([(75, 95)], (2.8, 0.35), label="Spoofing Window")
    ax.broken_barh([(90, 75)], (1.8, 0.35), label="Tampering Window")
    ax.broken_barh([(100, 45)], (0.8, 0.35), label="Combined Degradation")

    ax.axvline(66, linestyle="--", linewidth=1)
    ax.text(66, 4.45, "Detection", rotation=90, va="bottom", fontsize=9)

    ax.axvline(82, linestyle="--", linewidth=1)
    ax.text(82, 4.45, "Adaptive Action", rotation=90, va="bottom", fontsize=9)

    ax.axvline(120, linestyle="--", linewidth=1)
    ax.text(120, 4.45, "Recovery", rotation=90, va="bottom", fontsize=9)

    ax.set_yticks([4, 3, 2, 1])
    ax.set_yticklabels(["RF Link", "GNSS/Nav", "Mission Logs", "Mission State"])
    ax.set_xlabel("Mission Time Step")
    ax.set_ylim(0.5, 4.8)
    ax.legend(loc="lower right")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "figure_v3_attack_timeline.png", dpi=600)
    fig.savefig(OUT_DIR / "figure_v3_attack_timeline.pdf")
    plt.close(fig)


def digital_twin_action_selection():
    actions = ["Continue", "Monitor", "Reroute", "Reassign", "Isolate Node", "Return to Base"]
    projected = [0.58, 0.62, 0.71, 0.78, 0.74, 0.66]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(actions, projected)
    ax.set_ylim(0, 1)
    ax.set_ylabel("Projected Mission Assurance")
    ax.set_xlabel("Candidate Action")
    ax.set_title("Digital Twin Candidate Action Selection")
    ax.tick_params(axis="x", rotation=30)
    ax.axhline(max(projected), linestyle="--", linewidth=1)
    ax.text(3, max(projected) + 0.03, "Selected action: Reassign", ha="center", fontsize=10)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "figure_v3_digital_twin_action_selection.png", dpi=600)
    fig.savefig(OUT_DIR / "figure_v3_digital_twin_action_selection.pdf")
    plt.close(fig)


def experimental_pipeline():
    fig, ax = plt.subplots(figsize=(13, 5.5))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 5.5)
    ax.axis("off")

    ax.set_title("RA-MARS v3 Experimental Evaluation Pipeline", fontsize=14, fontweight="bold")

    steps = [
        ("Synthetic\nMission Simulation", 0.4),
        ("Sequence-Safe\nSampling", 2.4),
        ("20-Step\nWindowing", 4.4),
        ("Non-Leakage\nFeature Set", 6.4),
        ("Model\nTraining", 8.4),
        ("Mission-Level\nEvaluation", 10.4),
    ]

    for text, x in steps:
        box(ax, x, 2.7, 1.5, 1.0, text, fs=9)

    for i in range(len(steps) - 1):
        arrow(ax, steps[i][1] + 1.5, 3.2, steps[i + 1][1], 3.2)

    ax.text(
        6.5,
        1.3,
        "Outputs: model performance, confusion matrix, ablation results, Mission Assurance Index, scalability and attack-intensity stress tests",
        ha="center",
        fontsize=10,
    )

    save(fig, "figure_v3_experimental_pipeline")


def main():
    cross_layer_architecture()
    closed_loop_workflow()
    mai_components()
    attack_timeline()
    digital_twin_action_selection()
    experimental_pipeline()

    print(f"Saved conceptual v3 figures to {OUT_DIR}")
    for f in sorted(OUT_DIR.glob("*")):
        print(f)


if __name__ == "__main__":
    main()
