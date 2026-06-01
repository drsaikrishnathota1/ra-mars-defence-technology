#!/bin/bash
set -e

echo "Starting RA-MARS v3 full RunPod pipeline..."

source .venv/bin/activate

echo "Step 1: Generate v3 dataset"
python simulations/python/generate_dataset_v3.py

echo "Step 2: Create v3 sequence windows"
python simulations/python/create_sequence_windows_v3.py

echo "Step 3: Train v3 classical sequence models"
python simulations/python/train_classical_models_v3.py

echo "Step 4: Train v3 deep sequence models"
python simulations/python/train_sequence_models_v3.py

echo "RA-MARS v3 RunPod pipeline completed."
