"""
RA-MARS v3 Deep Sequence Model Training

Trains GRU and LSTM models on UAV telemetry sequence windows.

Input:
- simulations/datasets/uav_sequence_windows_v3.npz

Outputs:
- simulations/results/model_performance_v3_sequence.csv
"""

import os
import random
import numpy as np
import pandas as pd
import torch
import torch.nn as nn

from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


DATA_PATH = "simulations/datasets/uav_sequence_windows_v3.npz"
OUTPUT_DIR = "simulations/results"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "model_performance_v3_sequence.csv")

RANDOM_SEED = 42
BATCH_SIZE = 64
EPOCHS = 20
LEARNING_RATE = 0.001
HIDDEN_SIZE = 64
NUM_LAYERS = 1


def set_seed(seed=RANDOM_SEED):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)


class GRUClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes):
        super().__init__()
        self.gru = nn.GRU(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
        )
        self.fc = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        _, h = self.gru(x)
        out = h[-1]
        return self.fc(out)


class LSTMClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes):
        super().__init__()
        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
        )
        self.fc = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        _, (h, _) = self.lstm(x)
        out = h[-1]
        return self.fc(out)


def load_data():
    data = np.load(DATA_PATH, allow_pickle=True)
    X = data["X"].astype(np.float32)
    y = data["y"].astype(np.int64)
    labels = data["labels"]

    return X, y, labels


def make_loaders(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=RANDOM_SEED,
        stratify=y,
    )

    train_ds = TensorDataset(
        torch.tensor(X_train, dtype=torch.float32),
        torch.tensor(y_train, dtype=torch.long),
    )
    test_ds = TensorDataset(
        torch.tensor(X_test, dtype=torch.float32),
        torch.tensor(y_test, dtype=torch.long),
    )

    train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True)
    test_loader = DataLoader(test_ds, batch_size=BATCH_SIZE, shuffle=False)

    return train_loader, test_loader, y_test


def train_model(model, train_loader, device):
    criterion = nn.CrossEntropyLoss()
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

        avg_loss = total_loss / max(1, len(train_loader))
        print(f"Epoch {epoch:02d}/{EPOCHS} - loss: {avg_loss:.4f}")


def evaluate_model(model, test_loader, y_test, labels, device):
    model.eval()
    preds = []

    with torch.no_grad():
        for X_batch, _ in test_loader:
            X_batch = X_batch.to(device)
            logits = model(X_batch)
            batch_preds = torch.argmax(logits, dim=1).cpu().numpy()
            preds.extend(batch_preds)

    preds = np.array(preds)

    return {
        "accuracy": accuracy_score(y_test, preds),
        "precision_macro": precision_score(y_test, preds, average="macro", zero_division=0),
        "recall_macro": recall_score(y_test, preds, average="macro", zero_division=0),
        "f1_macro": f1_score(y_test, preds, average="macro", zero_division=0),
        "precision_weighted": precision_score(y_test, preds, average="weighted", zero_division=0),
        "recall_weighted": recall_score(y_test, preds, average="weighted", zero_division=0),
        "f1_weighted": f1_score(y_test, preds, average="weighted", zero_division=0),
    }


def main():
    set_seed()
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    X, y, labels = load_data()
    train_loader, test_loader, y_test = make_loaders(X, y)

    input_size = X.shape[2]
    num_classes = len(labels)

    configs = [
        ("GRU", GRUClassifier(input_size, HIDDEN_SIZE, NUM_LAYERS, num_classes)),
        ("LSTM", LSTMClassifier(input_size, HIDDEN_SIZE, NUM_LAYERS, num_classes)),
    ]

    results = []

    for name, model in configs:
        print(f"\nTraining {name} model...")
        model = model.to(device)

        train_model(model, train_loader, device)
        metrics = evaluate_model(model, test_loader, y_test, labels, device)
        metrics["model"] = name
        results.append(metrics)

        print(metrics)

    results_df = pd.DataFrame(results)
    cols = ["model"] + [c for c in results_df.columns if c != "model"]
    results_df = results_df[cols]
    results_df.to_csv(OUTPUT_PATH, index=False)

    print(f"\nSaved sequence model results: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
