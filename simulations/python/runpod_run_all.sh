#!/bin/bash
# RA-MARS v4 RunPod Master Script
# Runs all 7 steps in sequence on a single GPU pod
# Expected runtime: ~45-90 mins on RTX 4090
# Expected cost: ~$0.50-$0.70

set -e  # stop on any error

echo "=============================================="
echo "RA-MARS v4 Full Pipeline — RunPod"
echo "=============================================="
echo "Started: $(date)"
echo ""

# ── Setup ──────────────────────────────────────────────────────
cd /workspace

# Clone repo (replace with your actual GitHub URL)
if [ ! -d "ra-mars-defence-technology" ]; then
    git clone https://github.com/drsaikrishnathota1/ra-mars-defence-technology.git
fi
cd ra-mars-defence-technology

# Install dependencies
echo "Installing dependencies..."
pip install numpy pandas scikit-learn torch scipy matplotlib seaborn foolbox --quiet

# Create output dirs
mkdir -p simulations/datasets simulations/results

# ── Step 1: Generate v4 dataset ───────────────────────────────
echo ""
echo "STEP 1/7: Generating v4 physics-based dataset..."
echo "  (Friis RF model, SINR-based PDR, energy model)"
python simulations/python/generate_dataset_v4.py
echo "  ✓ Step 1 complete"

# ── Step 2: Create sequence windows ───────────────────────────
echo ""
echo "STEP 2/7: Creating sequence windows for LSTM..."
python simulations/python/create_sequence_windows_v4.py
echo "  ✓ Step 2 complete"

# ── Step 3: Train LSTM/GRU models ─────────────────────────────
echo ""
echo "STEP 3/7: Training v4 binary + fine-grained LSTM/GRU..."
echo "  (focal loss, 2-layer LSTM hidden=128, early stopping)"
python simulations/python/train_sequence_models_v4.py
echo "  ✓ Step 3 complete"

# ── Step 4: Train classical models ────────────────────────────
echo ""
echo "STEP 4/7: Training classical models (RF, SVM, LR)..."
python simulations/python/train_classical_models_v3.py
echo "  ✓ Step 4 complete"

# ── Step 5: Ablation + mission evaluation ─────────────────────
echo ""
echo "STEP 5/7: Running ablation + mission assurance evaluation..."
python simulations/python/evaluate_ablation_v4.py
echo "  ✓ Step 5 complete"

# ── Step 6: Adversarial robustness ────────────────────────────
echo ""
echo "STEP 6/7: Running FGSM + PGD adversarial robustness tests..."
# Model files now saved by train_sequence_models_v4.py
ls simulations/results/best_model_v4_*.pt 2>/dev/null && echo "Model files found" || echo "No model files"
python simulations/python/adversarial_robustness_v4.py
echo "  ✓ Step 6 complete"

# ── Step 7: Latency budget ────────────────────────────────────
echo ""
echo "STEP 7/7: Computing latency budget analysis..."
python simulations/python/latency_budget_v4.py
echo "  ✓ Step 7 complete"

# ── Summary ───────────────────────────────────────────────────
echo ""
echo "=============================================="
echo "ALL STEPS COMPLETE"
echo "Finished: $(date)"
echo ""
echo "Results generated:"
ls -lh simulations/results/*.csv 2>/dev/null | awk '{print "  "$5, $9}'
echo ""
echo "NEXT: Download simulations/results/ folder"
echo "      and simulations/datasets/uav_mission_telemetry_v4_sample.csv"
echo "=============================================="
