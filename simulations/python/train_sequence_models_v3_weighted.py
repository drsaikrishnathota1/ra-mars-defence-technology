"""
RA-MARS v3 Weighted Deep Sequence Model Training

Uses class-weighted cross-entropy to improve minority attack-class detection.
Input:
- simulations/datasets/uav_sequence_windows_v3.npz

Output:
- simulations/results/model_performance_v3_sequence_weighted.csv
"""

import os
import random
import numpy as np
import pandas as pd
import torch
import torch.nn as nn

from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix


DATA_PATH = "simulations/datasets/uav_sequence_windows_v3.npz"
OUTPUT_DIR = "simulations/results"

PERFORMANCE_PATH = os.path.join(OUTPUT_DIR, "model_performance_v3_sequence_weighted.csv")
PER_CLASS_PATH = os.path.join(OUTPUT_DIR, "per_class_metrics_v3_sequence_weighted.csv")
CONFUSION_PATH = os.path.join(OUTPUT_DIR, "confusion_matrix_v3_sequence_weighted.csv")

RANDOM_SEED = 42
BATCH_SIZE = 64
EPOCHS = 10
LEARNING_RATE = 0.001
HIDDEN_SIZE = 48
NUM_LAYERS = 1


def set_seed(seed=RANDOM_SEED):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)


class GRUClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes):
        super().__init__()
        self.gru = nn.GRU(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        _, h = self.gru(x)
        return self.fc(h[-1])


class LSTMClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        _, (h, _) = self.lstm(x)
        return self.fc(h[-1])


def load_data():
    data = np.load(DATA_PATH, allow_pickle=True)
    X = data["X"].astype(np.float32)
    y = data["y"].astype(np.int64)
    labels = data["labels"]
    return X, y, labels


def make_loaders(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=RANDOM_SEED, stratify=y
    )

    train_loader = DataLoader(
        TensorDataset(torch.tensor(X_train), torch.tensor(y_train)),
        batch_size=BATCH_SIZE,
        shuffle=True,
    )

    test_loader = DataLoader(
        TensorDataset(torch.tensor(X_test), torch.tensor(y_test)),
        batch_size=BATCH_SIZE,
        shuffle=False,
    )

    return train_loader, test_loader, y_train, y_test


def class_weights(y_train, num_classes):
    counts = np.bincount(y_train, minlength=num_classes)
    weights = counts.sum() / (num_classes * np.maximum(counts, 1))
    return torch.tensor(weights, dtype=torch.float32)


def train_model(model, train_loader, device, weights):
    criterion = nn.CrossEntropyLoss(weight=weights.to(device))
    optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)

    model.train()
    for epoch in range(1, EPOCHS + 1):
        total_loss = 0.0

        for X_batch, y_batch in train_loader:
            X_batch = X_batch.to(device)
            y_batch = y_batch.to(device)

            optimizer.zero_grad()
            logits = model(X_batch)
            loss = criterion(logits, y_batch)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        print(f"Epoch {epoch:02d}/{EPOCHS} - loss: {total_loss / max(1, len(train_loader)):.4f}")


def evaluate_model(name, model, test_loader, y_test, labels, device):
    model.eval()
    preds = []

    with torch.no_grad():
        for X_batch, _ in test_loader:
            X_batch = X_batch.to(device)
            logits = model(X_batch)
            preds.extend(torch.argmax(logits, dim=1).cpu().numpy())

    preds = np.array(preds)

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
        y_test, preds, target_names=labels, output_dict=True, zero_division=0
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
    set_seed()
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    X, y, labels = load_data()
    train_loader, test_loader, y_train, y_test = make_loaders(X, y)

    input_size = X.shape[2]
    num_classes = len(labels)
    weights = class_weights(y_train, num_classes)

    print("Class weights:", weights.numpy())

    configs = [
        ("Weighted GRU", GRUClassifier(input_size, HIDDEN_SIZE, NUM_LAYERS, num_classes)),
        ("Weighted LSTM", LSTMClassifier(input_size, HIDDEN_SIZE, NUM_LAYERS, num_classes)),
    ]

    results = []
    per_class_all = []
    best_f1 = -1
    best_cm = None
    best_model = None

    for name, model in configs:
        print(f"\nTraining {name}...")
        model = model.to(device)

        train_model(model, train_loader, device, weights)
        perf, per_class_rows, cm_df = evaluate_model(name, model, test_loader, y_test, labels, device)

        print(perf)

        results.append(perf)
        per_class_all.extend(per_class_rows)

        if perf["f1_macro"] > best_f1:
            best_f1 = perf["f1_macro"]
            best_cm = cm_df
            best_model = name

    pd.DataFrame(results).to_csv(PERFORMANCE_PATH, index=False)
    pd.DataFrame(per_class_all).to_csv(PER_CLASS_PATH, index=False)
    best_cm.to_csv(CONFUSION_PATH)

    print(f"Saved weighted sequence performance: {PERFORMANCE_PATH}")
    print(f"Saved weighted per-class metrics: {PER_CLASS_PATH}")
    print(f"Saved weighted confusion matrix for {best_model}: {CONFUSION_PATH}")


if __name__ == "__main__":
    main()
