from pathlib import Path
import csv
import math

ROOT = Path(".")
FINAL = ROOT / "simulations" / "final-results"
RESULTS = ROOT / "simulations" / "results"
OUT = ROOT / "figures" / "graphs" / "v4"
OUT.mkdir(parents=True, exist_ok=True)

def read_csv(path):
    with Path(path).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def fnum(x, default=0.0):
    try:
        return float(x)
    except Exception:
        return default

def short_label(s, maxlen=18):
    s = str(s)
    return s if len(s) <= maxlen else s[:maxlen-1] + "…"

def bar_svg(path, title, labels, values, ylabel="", width=1100, height=650):
    margin_left, margin_right = 90, 40
    margin_top, margin_bottom = 80, 150
    plot_w = width - margin_left - margin_right
    plot_h = height - margin_top - margin_bottom

    max_val = max(values) if values else 1
    if max_val <= 0:
        max_val = 1
    y_max = math.ceil(max_val * 1.15 / 10) * 10 if max_val > 10 else max_val * 1.15

    n = len(values)
    gap = 12
    bar_w = max(16, (plot_w - gap * (n + 1)) / max(n, 1))

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">')
    svg.append('<rect width="100%" height="100%" fill="white"/>')
    svg.append(f'<text x="{width/2}" y="40" text-anchor="middle" font-family="Arial" font-size="24" font-weight="bold">{title}</text>')

    # axes
    x0, y0 = margin_left, height - margin_bottom
    svg.append(f'<line x1="{x0}" y1="{margin_top}" x2="{x0}" y2="{y0}" stroke="black" stroke-width="2"/>')
    svg.append(f'<line x1="{x0}" y1="{y0}" x2="{width-margin_right}" y2="{y0}" stroke="black" stroke-width="2"/>')
    if ylabel:
        svg.append(f'<text x="25" y="{height/2}" transform="rotate(-90 25,{height/2})" text-anchor="middle" font-family="Arial" font-size="16">{ylabel}</text>')

    # y ticks
    for i in range(6):
        val = y_max * i / 5
        y = y0 - (val / y_max) * plot_h
        svg.append(f'<line x1="{x0-5}" y1="{y:.1f}" x2="{x0}" y2="{y:.1f}" stroke="black"/>')
        svg.append(f'<text x="{x0-10}" y="{y+5:.1f}" text-anchor="end" font-family="Arial" font-size="12">{val:.1f}</text>')
        svg.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{width-margin_right}" y2="{y:.1f}" stroke="#ddd"/>')

    # bars
    for i, (lab, val) in enumerate(zip(labels, values)):
        x = x0 + gap + i * (bar_w + gap)
        h = (val / y_max) * plot_h
        y = y0 - h
        svg.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{h:.1f}" fill="#4a78c2"/>')
        svg.append(f'<text x="{x+bar_w/2:.1f}" y="{y-8:.1f}" text-anchor="middle" font-family="Arial" font-size="12">{val:.2f}</text>')
        svg.append(f'<text x="{x+bar_w/2:.1f}" y="{y0+18}" text-anchor="end" transform="rotate(-45 {x+bar_w/2:.1f},{y0+18})" font-family="Arial" font-size="12">{short_label(lab)}</text>')

    svg.append('</svg>')
    Path(path).write_text("\n".join(svg), encoding="utf-8")
    print(f"Created {path}")

# Figure 1: model F1 comparison
labels, values = [], []
for file in ["model_performance_v4_binary.csv", "model_performance_v4_finegrained.csv"]:
    for r in read_csv(FINAL / file):
        labels.append(r["model"])
        values.append(fnum(r["f1_macro"]) * 100)
bar_svg(OUT / "figure_v4_model_f1_comparison.svg", "RA-MARS v4 Model Macro-F1 Comparison", labels, values, "Macro-F1 (%)")

# Figure 2: mission success by scenario
rows = read_csv(FINAL / "mission_assurance_index_v4.csv")
labels = [f'{r["scenario"]}-{r["attack_intensity"]}' for r in rows]
values = [fnum(r["mission_success_rate_mean"]) for r in rows]
bar_svg(OUT / "figure_v4_mission_success_by_scenario.svg", "RA-MARS v4 Mission Success by Scenario", labels, values, "Mission Success (%)")

# Figure 3: ablation mission success
rows = read_csv(FINAL / "ablation_results_v4.csv")
labels = [r["method"] for r in rows]
values = [fnum(r["mission_success_rate_mean"]) for r in rows]
bar_svg(OUT / "figure_v4_ablation_mission_success.svg", "RA-MARS v4 Ablation Study", labels, values, "Mission Success (%)")

# Figure 4: RF/SINR validation
rows = read_csv(FINAL / "rf_sinr_summary_v4.csv")
labels = [f'{r["scenario"]}-{r["attack_intensity"]}' for r in rows]
values = [fnum(r["sinr_mean_db"]) for r in rows]
bar_svg(OUT / "figure_v4_rf_sinr_validation.svg", "RA-MARS v4 RF/SINR Validation", labels, values, "Mean SINR (dB)")

# Figure 5: detection delay
rows = read_csv(FINAL / "detection_delay_v4.csv")
labels = [f'{r["actual_attack_type"]}-{r["attack_intensity"]}' for r in rows]
values = [fnum(r["detection_delay_mean"]) for r in rows]
bar_svg(OUT / "figure_v4_detection_delay.svg", "RA-MARS v4 Detection Delay", labels, values, "Delay (s)")

# Figure 6: adversarial training robustness
adv_path = RESULTS / "adversarial_training_results_v4.csv"
if adv_path.exists():
    rows = read_csv(adv_path)
    labels = [f'{r["attack"]} ε={r["epsilon"]}' for r in rows]
    values = [fnum(r["adv_f1"]) * 100 for r in rows]
    bar_svg(OUT / "figure_v4_adversarial_training_robustness.svg", "RA-MARS v4 Adversarial Training Robustness", labels, values, "Adversarial Macro-F1 (%)")
else:
    print("Skipped adversarial training figure: missing simulations/results/adversarial_training_results_v4.csv")

print("All available v4 SVG figures generated.")
