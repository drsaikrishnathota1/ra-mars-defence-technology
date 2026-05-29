"""
RA-MARS v2 Result Table Generator

Creates markdown result tables for the manuscript from v2 CSV outputs.
"""

from pathlib import Path
import pandas as pd


RESULTS_DIR = Path("simulations/results")
TABLES_DIR = Path("tables/final")
TABLES_DIR.mkdir(parents=True, exist_ok=True)


def write_table(df, path, title):
    with open(path, "w") as f:
        f.write(f"# {title}\n\n")
        f.write(df.to_markdown(index=False))
        f.write("\n")


def main():
    model = pd.read_csv(RESULTS_DIR / "model_performance_v2.csv")
    mission = pd.read_csv(RESULTS_DIR / "mission_success_results_v2.csv")
    comm = pd.read_csv(RESULTS_DIR / "communication_results_v2.csv")
    nav = pd.read_csv(RESULTS_DIR / "navigation_results_v2.csv")
    tamper = pd.read_csv(RESULTS_DIR / "tamper_detection_results_v2.csv")
    energy = pd.read_csv(RESULTS_DIR / "energy_results_v2.csv")
    recovery = pd.read_csv(RESULTS_DIR / "recovery_time_results_v2.csv")

    model_rounded = model.copy()
    for col in ["accuracy", "precision_macro", "recall_macro", "f1_macro"]:
        model_rounded[col] = model_rounded[col].round(4)

    write_table(
        model_rounded,
        TABLES_DIR / "table_ai_detection_performance_v2.md",
        "Table: AI Attack Detection Performance",
    )

    mission_pivot = mission.pivot(
        index="scenario",
        columns="method",
        values="mission_success_rate",
    ).round(2).reset_index()

    write_table(
        mission_pivot,
        TABLES_DIR / "table_mission_success_v2.md",
        "Table: Mission Success Rate Across Scenarios",
    )

    comm_summary = comm.copy()
    comm_summary["packet_delivery_ratio"] = comm_summary["packet_delivery_ratio"].round(3)
    comm_summary["avg_latency_ms"] = comm_summary["avg_latency_ms"].round(2)

    write_table(
        comm_summary,
        TABLES_DIR / "table_communication_results_v2.md",
        "Table: Communication Performance",
    )

    nav_pivot = nav.pivot(
        index="scenario",
        columns="method",
        values="avg_route_deviation",
    ).round(2).reset_index()

    write_table(
        nav_pivot,
        TABLES_DIR / "table_navigation_results_v2.md",
        "Table: Average Route Deviation",
    )

    tamper_pivot = tamper.pivot(
        index="scenario",
        columns="method",
        values="tamper_detection_rate",
    ).round(2).reset_index()

    write_table(
        tamper_pivot,
        TABLES_DIR / "table_tamper_detection_v2.md",
        "Table: Tamper-Detection Rate",
    )

    energy_pivot = energy.pivot(
        index="scenario",
        columns="method",
        values="energy_consumption",
    ).round(2).reset_index()

    write_table(
        energy_pivot,
        TABLES_DIR / "table_energy_consumption_v2.md",
        "Table: Energy Consumption",
    )

    recovery_pivot = recovery.pivot(
        index="scenario",
        columns="method",
        values="mission_recovery_time_sec",
    ).round(2).reset_index()

    write_table(
        recovery_pivot,
        TABLES_DIR / "table_recovery_time_v2.md",
        "Table: Mission Recovery Time",
    )

    print(f"Generated final markdown tables in {TABLES_DIR}")


if __name__ == "__main__":
    main()
