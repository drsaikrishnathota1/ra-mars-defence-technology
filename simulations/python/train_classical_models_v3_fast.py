"""
RA-MARS v3 Fast Classical Model Training

Fast non-leakage baseline on sequence windows.
Skips slow Gradient Boosting.
"""

import os
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
)
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC


DATA_PATH = "simulations/datasets/uav_sequence_windows_v3.npz"
OUTPUT_DIR = "simulations/results"

PERFORMANCE_PATH = os.path.join(OUTPUT_DIR, "model_performance_v3_classical.csv")
PER_CLASS_PATH = os.path.join(OUTPUT_DIR, "per_class_metrics_v3_classical.csv")
CONFUSION_PATH = os.path.join(OUTPUT_DIR, "confusion_matrix_v3_classical.csv")


def load_data():
    data = np.load(DATA_PATH, allow_pickle=True)
    X = data["X"]
    y = data["y"]
    labels = data["labels"]

    n_samples, window_size, n_features = X.shape
    X_flat = X.reshape(n_samples, window_size * n_features)

    print(f"Loaded X shape: {X.shape}")
    print(f"Flattened X shape: {X_flat.shape}")
    print(f"Labels: {labels}")

    return X_flat, y, labels


def evaluate_model(name, model, X_train, X_test, y_train, y_test, labels):
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    performance = {
        "model": name,
        "accuracy": accuracy_score(y_test, preds),
        "precision_macro": precision_score(y_test, preds, average="macro", zero_division=0),
        "recall_macro": recall_score(y_test, preds, average="macro", zero_division=0),
        "f1_macro": f1_score(y_test, preds, average="macro", zero_division=0),
        "precision_weighted": precision_score(y_test, preds, average="weighted", zero_division=0),
        "recall_weighted": recall_score(y_test, preds, average="weighted", zero_division=0),
        "f1_weighted": f1_score(y_test, preds, average="weighted", zero_division=0),
    }

    report = classification_report(
        y_test,
        preds,
        target_names=labels,
        output_dict=True,
        zero_division=0,
    )

    per_class_rows = []
    for label in labels:
        metrics = report[label]
        per_class_rows.append({
            "model": name,
            "class": label,
            "precision": metrics["precision"],
            "recall": metrics["recall"],
            "f1_score": metrics["f1-score"],
            "support": metrics["support"],
        })

    cm = confusion_matrix(y_test, preds)
    cm_df = pd.DataFrame(cm, index=labels, columns=labels)

    return performance, per_class_rows, cm_df


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    X, y, labels = load_data()

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y,
    )

    models = [
        ("Logistic Regression", LogisticRegression(max_iter=1000)),
        ("Linear SVM", LinearSVC(max_iter=3000)),
        (
            "Random Forest",
            RandomForestClassifier(
                n_estimators=120,
                max_depth=16,
                random_state=42,
                n_jobs=-1,
            ),
        ),
    ]

    performances = []
    per_class_all = []
    best_model_name = None
    best_f1 = -1
    best_cm = None

    for name, model in models:
        print(f"Training {name}...")
        perf, per_class_rows, cm_df = evaluate_model(
            name, model, X_train, X_test, y_train, y_test, labels
        )

        performances.append(perf)
        per_class_all.extend(per_class_rows)

        print(perf)

        if perf["f1_macro"] > best_f1:
            best_f1 = perf["f1_macro"]
            best_model_name = name
            best_cm = cm_df

    pd.DataFrame(performances).to_csv(PERFORMANCE_PATH, index=False)
    pd.DataFrame(per_class_all).to_csv(PER_CLASS_PATH, index=False)
    best_cm.to_csv(CONFUSION_PATH)

    print(f"Saved performance: {PERFORMANCE_PATH}")
    print(f"Saved per-class metrics: {PER_CLASS_PATH}")
    print(f"Saved confusion matrix for best model ({best_model_name}): {CONFUSION_PATH}")


if __name__ == "__main__":
    main()
