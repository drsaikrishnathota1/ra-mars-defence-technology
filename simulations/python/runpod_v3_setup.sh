#!/bin/bash
set -e

echo "Setting up RA-MARS v3 RunPod environment..."

python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install numpy pandas scikit-learn matplotlib tabulate torch xgboost lightgbm

echo "RunPod environment setup completed."
