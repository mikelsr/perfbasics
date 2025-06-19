import json
import argparse
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import seaborn as sns

from pathlib import Path
from rich.console import Console
from rich.table import Table


def load_results(file_paths):
    results = []
    for path in file_paths:
        with open(path) as f:
            data = json.load(f)
            data["file"] = Path(path).name
            results.append(data)
    return results


def compare(results):
    base_time = results[0]["execution_time_seconds"]
    for result in results:
        time_sec = result["execution_time_seconds"]
        result["absolute_diff"] = time_sec - base_time
        result["percent_diff"] = ((time_sec - base_time) / base_time * 100) if base_time != 0 else 0
    return results


def print_table(results):
    table = Table(title="Benchmark Comparison")
    table.add_column("File", style="cyan")
    table.add_column("Time (s)", justify="right")
    table.add_column("Abs Δ (s)", justify="right")
    table.add_column("Δ (%)", justify="right")

    for r in results:
        table.add_row(
            r["file"], f"{r['execution_time_seconds']:.6f}", f"{r['absolute_diff']:+.6f}", f"{r['percent_diff']:+.2f}%"
        )

    console = Console()
    console.print(table)


# This function is not used, but I've kept it in case someone has issues with seaborn.


def plot_results(results, save_path=None):
    sns.set_theme(style="whitegrid")  # clean seaborn theme

    labels = [r["file"] for r in results]
    times = [r["execution_time_seconds"] for r in results]

    fig, ax = plt.subplots(figsize=(10, 6))
    bar_colors = sns.color_palette("pastel", len(results))
    bars = ax.bar(labels, times, color=bar_colors, edgecolor="black", linewidth=0.6)

    # Y-axis formatting
    ax.set_ylabel("Execution Time (s)", fontsize=12)
    ax.set_title("Benchmark Execution Time Comparison", fontsize=14, pad=15)
    ax.set_ylim(0, max(times) * 1.2)  # Add some headroom

    # Gridlines
    ax.yaxis.grid(True, linestyle="--", linewidth=0.5)

    # Annotate bars with time and percent diff
    for bar, r in zip(bars, results):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + max(times) * 0.02,  # nudge above bar
            f"{height:.3f}s\n({r['percent_diff']:+.1f}%)",
            ha="center",
            va="bottom",
            fontsize=9,
            color="black",
        )

    # Optional save to file
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
        print(f"Saved chart to {save_path}")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare benchmark JSON files.")
    parser.add_argument("files", nargs="+", help="Benchmark JSON files to compare")
    args = parser.parse_args()

    if len(args.files) < 2:
        print("Please provide at least two benchmark files.")
        exit(1)

    results = load_results(args.files)
    results = compare(results)
    print_table(results)
    try:
        plot_results(results)
    except KeyboardInterrupt:
        pass
