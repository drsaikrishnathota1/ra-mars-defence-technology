"""
RA-MARS v3 Journal Figure Generator

Creates journal-style figures from optimized v3 results.
"""

from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


RESULTS_DIR = Path("simulations/results")
DATASETS_DIR = Path("simulations/datasets")
OUT_DIR = Path("figures/graphs/v3")
OUT_DIR.mkdir(parents=True, exist_ok=True)


def save_model_comparison():
    df = pd.read_csv(RESULTS_DIR / "model_performance_v3_combined_summary.csv")
    df = df.sort_values("f1_macro", ascending=False)

    plt.figure(figsize=(10, 6))
    plt.bar(df["model"], df["f1_macro"])
    plt.ylabel("Macro F1-score")
    plt.xlabel("Model")
    plt.title("RA-MARS v3 Attack Detection Model Comparison")
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "v3_model_comparison_macro_f1.png", dpi=600)
    plt.savefig(OUT_DIR / "v3_model_comparison_macro_f1.pdf")
    plt.close()


def save_accuracy_comparison():
    df = pd.read_csv(RESULTS_DIR / "model_performance_v3_combined_summary.csv")
    df = df.sort_values("accuracy", ascending=False)

    plt.figure(figsize=(10, 6))
    plt.bar(df["model"], df["accuracy"])
    plt.ylabel("Accuracy")
    plt.xlabel("Model")
    plt.title("RA-MARS v3 Attack Detection Accuracy")
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "v3_model_comparison_accuracy.png", dpi=600)
    plt.savefig(OUT_DIR / "v3_model_comparison_accuracy.pdf")
    plt.close()


def save_per_class_f1():
    candidates = [
        RESULTS_DIR / "per_class_metrics_v3_sequence_weighted.csv",
        RESULTS_DIR / "per_class_metrics_v3_classical.csv",
    ]

    rows = []
    for path in candidates:
        if path.exists():
            df = pd.read_csv(path)
            rows.append(df)

    if not rows:
        return

    df = pd.concat(rows, ignore_index=True)

    best_model = (
        pd.read_csv(RESULTS_DIR / "model_performance_v3_combined_summary.csv")
        .sort_values("f1_macro", ascending=False)
        .iloc[0]["model"]
    )

    plot_df = df[df["model"] == best_model].copy()
    if plot_df.empty:
        plot_df = df.copy()

    plt.figure(figsize=(11, 6))
    plt.bar(plot_df["class"], plot_df["f1_score"])
    plt.ylabel("F1-score")
    plt.xlabel("Attack Class")
    plt.title(f"Per-Class F1-score for {best_model}")
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "v3_per_class_f1.png", dpi=600)
    plt.savefig(OUT_DIR / "v3_per_class_f1.pdf")
    plt.close()


def save_confusion_matrix():
    cm_path = RESULTS_DIR / "confusion_matrix_v3_sequence_weighted.csv"
    if not cm_path.exists():
        cm_path = RESULTS_DIR / "confusion_matrix_v3_classical.csv"

    cm = pd.read_csv(cm_path, index_col=0)

    plt.figure(figsize=(9, 8))
    plt.imshow(cm.values, aspect="auto")
    plt.colorbar(label="Count")
    plt.xticks(range(len(cm.columns)), cm.columns, rotation=45, ha="right")
    plt.yticks(range(len(cm.index)), cm.index)
    plt.xlabel("Predicted Class")
    plt.ylabel("True Class")
    plt.title("RA-MARS v3 Confusion Matrix")

    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, str(cm.values[i, j]), ha="center", va="center", fontsize=7)

    plt.tight_layout()
    plt.savefig(OUT_DIR / "v3_confusion_matrix.png", dpi=600)
    plt.savefig(OUT_DIR / "v3_confusion_matrix.pdf")
    plt.close()


def save_class_distribution():
    df = pd.read_csv(DATASETS_DIR / "sequence_label_distribution_v3.csv")

    plt.figure(figsize=(10, 6))
    plt.bar(df["label"], df["count"])
    plt.ylabel("Number of Sequence Windows")
    plt.xlabel("Class")
    plt.title("RA-MARS v3 Sequence Window Class Distribution")
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "v3_sequence_class_distribution.png", dpi=600)
    plt.savefig(OUT_DIR / "v3_sequence_class_distribution.pdf")
    plt.close()


def main():
    save_model_comparison()
    save_accuracy_comparison()
    save_per_class_f1()
    save_confusion_matrix()
    save_class_distribution()

    print(f"Saved v3 journal figures to {OUT_DIR}")
    for f in sorted(OUT_DIR.glob("*")):
        print(f)


if __name__ == "__main__":
    main()
