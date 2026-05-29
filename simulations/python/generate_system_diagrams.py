"""
RA-MARS System Diagram Generator

Creates:
- RA-MARS architecture figure
- RA-MARS threat model figure
"""

import os
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch


OUTPUT_DIR = "figures/architecture/final"
THREAT_OUTPUT_DIR = "figures/threat-model/final"


def add_box(ax, xy, width, height, text, fontsize=9):
    box = Rectangle(xy, width, height, fill=False, linewidth=1.5)
    ax.add_patch(box)
    ax.text(
        xy[0] + width / 2,
        xy[1] + height / 2,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        wrap=True,
    )


def add_arrow(ax, start, end):
    arrow = FancyArrowPatch(
        start,
        end,
        arrowstyle="->",
        mutation_scale=12,
        linewidth=1.2,
    )
    ax.add_patch(arrow)


def architecture_figure():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    fig, ax = plt.subplots(figsize=(13, 7))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 7)
    ax.axis("off")

    ax.set_title(
        "RA-MARS System Architecture for Secure Multi-UAV Defence Surveillance",
        fontsize=14,
        fontweight="bold",
    )

    add_box(ax, (0.5, 4.7), 2.0, 1.0, "Multi-UAV\nSurveillance Layer")
    add_box(ax, (0.5, 3.1), 2.0, 1.0, "Telemetry:\nPosition, Battery,\nMission Status")
    add_box(ax, (3.1, 3.9), 2.0, 1.0, "Communication\nLayer")
    add_box(ax, (5.7, 3.9), 2.0, 1.0, "Ground Control\nStation")

    add_box(ax, (8.2, 5.4), 2.0, 0.8, "AI Attack\nDetection")
    add_box(ax, (8.2, 4.2), 2.0, 0.8, "Mission-Risk\nScoring")
    add_box(ax, (8.2, 3.0), 2.0, 0.8, "Adaptive Mission\nContinuation")
    add_box(ax, (8.2, 1.8), 2.0, 0.8, "Tamper-Resistant\nLogging")

    add_box(ax, (10.8, 3.2), 1.8, 1.2, "Mission Assurance\nOutput:\nContinuity,\nTrust, Recovery", fontsize=8)

    add_arrow(ax, (2.5, 5.2), (3.1, 4.4))
    add_arrow(ax, (2.5, 3.6), (3.1, 4.2))
    add_arrow(ax, (5.1, 4.4), (5.7, 4.4))
    add_arrow(ax, (7.7, 4.4), (8.2, 5.8))
    add_arrow(ax, (7.7, 4.4), (8.2, 4.6))
    add_arrow(ax, (7.7, 4.4), (8.2, 3.4))
    add_arrow(ax, (7.7, 4.4), (8.2, 2.2))

    add_arrow(ax, (10.2, 5.8), (10.8, 4.2))
    add_arrow(ax, (10.2, 4.6), (10.8, 4.0))
    add_arrow(ax, (10.2, 3.4), (10.8, 3.8))
    add_arrow(ax, (10.2, 2.2), (10.8, 3.4))

    ax.text(0.5, 0.6, "Figure 1. RA-MARS integrates AI detection, mission-risk scoring,\nadaptive response, and tamper-resistant logging for mission assurance.", fontsize=9)

    path = os.path.join(OUTPUT_DIR, "ra_mars_architecture.png")
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()
    print(f"Saved {path}")


def threat_model_figure():
    os.makedirs(THREAT_OUTPUT_DIR, exist_ok=True)

    fig, ax = plt.subplots(figsize=(13, 7))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 7)
    ax.axis("off")

    ax.set_title(
        "RA-MARS Threat Model for Multi-UAV Defence Surveillance",
        fontsize=14,
        fontweight="bold",
    )

    add_box(ax, (5.3, 3.3), 2.3, 1.1, "Multi-UAV\nMission Area")
    add_box(ax, (5.3, 1.3), 2.3, 0.9, "Ground Control\nStation")
    add_box(ax, (9.5, 1.3), 2.3, 0.9, "Mission Logs\nand Records")

    add_box(ax, (0.7, 5.4), 2.3, 0.9, "RF Jamming\nAttacker")
    add_box(ax, (5.0, 5.4), 2.8, 0.9, "GPS/GNSS Spoofing\nAttacker")
    add_box(ax, (9.7, 5.4), 2.3, 0.9, "Data-Tampering\nAttacker")

    add_box(ax, (9.5, 3.3), 2.3, 1.1, "RA-MARS\nDetection, Risk,\nAdaptive Response", fontsize=8)

    add_arrow(ax, (3.0, 5.8), (5.3, 4.1))
    add_arrow(ax, (6.4, 5.4), (6.4, 4.4))
    add_arrow(ax, (10.8, 5.4), (10.8, 2.2))

    add_arrow(ax, (6.4, 3.3), (6.4, 2.2))
    add_arrow(ax, (7.6, 3.8), (9.5, 3.8))
    add_arrow(ax, (10.6, 3.3), (10.6, 2.2))

    ax.text(0.7, 0.5, "Figure 2. Threat model showing RF jamming, GPS/GNSS spoofing,\nand mission-data tampering against multi-UAV surveillance.", fontsize=9)

    path = os.path.join(THREAT_OUTPUT_DIR, "ra_mars_threat_model.png")
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()
    print(f"Saved {path}")


def main():
    architecture_figure()
    threat_model_figure()


if __name__ == "__main__":
    main()
