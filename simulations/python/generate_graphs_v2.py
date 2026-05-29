"""
RA-MARS v2 Graph Generation Script

Generates publication-style result graphs from v2 CSV results.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt


RESULTS_DIR = "simulations/results"
OUTPUT_DIR = "figures/graphs/final"


def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def save_bar_chart(df, x_col, y_col, title, ylabel, filename, group_col=None):
    plt.figure(figsize=(10, 6))

    if group_col:
        pivot = df.pivot(index=x_col, columns=group_col, values=y_col)
        pivot.plot(kind="bar", figsize=(11, 6))
        plt.xlabel(x_col.replace("_", " ").title())
    else:
        plt.bar(df[x_col], df[y_col])
        plt.xlabel(x_col.replace("_", " ").title())

    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()

    output_path = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Saved {output_path}")


def main():
    ensure_output_dir()

    model_df = pd.read_csv(os.path.join(RESULTS_DIR, "model_performance_v2.csv"))
    mission_df = pd.read_csv(os.path.join(RESULTS_DIR, "mission_success_results_v2.csv"))
    comm_df = pd.read_csv(os.path.join(RESULTS_DIR, "communication_results_v2.csv"))
    nav_df = pd.read_csv(os.path.join(RESULTS_DIR, "navigation_results_v2.csv"))
    tamper_df = pd.read_csv(os.path.join(RESULTS_DIR, "tamper_detection_results_v2.csv"))
    energy_df = pd.read_csv(os.path.join(RESULTS_DIR, "energy_results_v2.csv"))
    recovery_df = pd.read_csv(os.path.join(RESULTS_DIR, "recovery_time_results_v2.csv"))

    save_bar_chart(
        model_df,
        "model",
        "f1_macro",
        "AI Attack Detection Performance",
        "Macro F1-Score",
        "graph1_ai_detection_performance_v2.png",
    )

    save_bar_chart(
        mission_df,
        "scenario",
        "mission_success_rate",
        "Mission Success Rate Across Scenarios",
        "Mission Success Rate (%)",
        "graph2_mission_success_rate_v2.png",
        group_col="method",
    )

    save_bar_chart(
        comm_df,
        "scenario",
        "packet_delivery_ratio",
        "Packet Delivery Ratio Across Scenarios",
        "Packet Delivery Ratio",
        "graph3_packet_delivery_ratio_v2.png",
        group_col="method",
    )

    save_bar_chart(
        comm_df,
        "scenario",
        "avg_latency_ms",
        "Average Latency Across Scenarios",
        "Average Latency (ms)",
        "graph4_average_latency_v2.png",
        group_col="method",
    )

    save_bar_chart(
        nav_df,
        "scenario",
        "avg_route_deviation",
        "Average Route Deviation Across Scenarios",
        "Route Deviation (m)",
        "graph5_route_deviation_v2.png",
        group_col="method",
    )

    tamper_only = tamper_df[tamper_df["scenario"].isin(["tampering", "combined"])]
    save_bar_chart(
        tamper_only,
        "scenario",
        "tamper_detection_rate",
        "Tamper Detection Rate",
        "Tamper Detection Rate",
        "graph6_tamper_detection_rate_v2.png",
        group_col="method",
    )

    save_bar_chart(
        energy_df,
        "scenario",
        "energy_consumption",
        "Energy Consumption Across Scenarios",
        "Energy Consumption (%)",
        "graph7_energy_consumption_v2.png",
        group_col="method",
    )

    save_bar_chart(
        recovery_df,
        "scenario",
        "mission_recovery_time_sec",
        "Mission Recovery Time Across Scenarios",
        "Recovery Time (s)",
        "graph8_mission_recovery_time_v2.png",
        group_col="method",
    )


if __name__ == "__main__":
    main()
