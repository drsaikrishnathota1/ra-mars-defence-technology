"""
RA-MARS v2 AI Model Training Script

Uses v2 dataset with row-level actual_attack_type labels.
Uses non-leakage telemetry features only.
Applies balanced sampling safely without losing label columns.
"""

import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import LinearSVC


DATA_PATH = "simulations/datasets/synthetic_uav_mission_data_v2_sample.csv"
OUTPUT_DIR = "simulations/results"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "model_performance_v2.csv")

FEATURES = [
    "packet_loss_rate",
    "latency_ms",
    "route_deviation",
    "gps_jump",
    "velocity_inconsistency",
    "battery_level",
    "mission_progress",
]


def load_balanced_data():
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(
            f"Dataset not found: {DATA_PATH}. Run generate_dataset_v2.py first."
        )

    df = pd.read_csv(DATA_PATH)

    if "actual_attack_type" not in df.columns:
        raise KeyError("actual_attack_type column not found in v2 dataset.")

    print("Class distribution before balancing:")
    print(df["actual_attack_type"].value_counts())

    min_class_count = df["actual_attack_type"].value_counts().min()

    sampled_parts = []
    for label in sorted(df["actual_attack_type"].unique()):
        class_df = df[df["actual_attack_type"] == label]
        sampled_parts.append(class_df.sample(n=min_class_count, random_state=42))

    balanced_df = (
        pd.concat(sampled_parts, ignore_index=True)
        .sample(frac=1.0, random_state=42)
        .reset_index(drop=True)
    )

    print("\nClass distribution after balancing:")
    print(balanced_df["actual_attack_type"].value_counts())

    X = balanced_df[FEATURES]
    y = balanced_df["actual_attack_type"]

    return train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y,
    )


def evaluate_model(name, model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    return {
        "model": name,
        "accuracy": accuracy_score(y_test, predictions),
        "precision_macro": precision_score(
            y_test, predictions, average="macro", zero_division=0
        ),
        "recall_macro": recall_score(
            y_test, predictions, average="macro", zero_division=0
        ),
        "f1_macro": f1_score(
            y_test, predictions, average="macro", zero_division=0
        ),
    }


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    X_train, X_test, y_train, y_test = load_balanced_data()

    models = [
        (
            "Logistic Regression",
            Pipeline(
                [
                    ("scaler", StandardScaler()),
                    ("model", LogisticRegression(max_iter=1000)),
                ]
            ),
        ),
        (
            "Linear SVM",
            Pipeline(
                [
                    ("scaler", StandardScaler()),
                    ("model", LinearSVC(max_iter=5000)),
                ]
            ),
        ),
        (
            "Random Forest",
            RandomForestClassifier(
                n_estimators=120,
                random_state=42,
                n_jobs=-1,
                max_depth=14,
            ),
        ),
        (
            "Gradient Boosting",
            GradientBoostingClassifier(random_state=42),
        ),
    ]

    results = []

    for name, model in models:
        print(f"\nTraining {name}...")
        result = evaluate_model(name, model, X_train, X_test, y_train, y_test)
        results.append(result)
        print(result)

    results_df = pd.DataFrame(results)
    results_df.to_csv(OUTPUT_PATH, index=False)

    print(f"\nSaved v2 model performance results to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
