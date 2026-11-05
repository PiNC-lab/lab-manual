from pathlib import Path

import matplotlib.pyplot as plt

from utils import load_counts, summarise_sites

HERE = Path(__file__).parent
DATA = HERE / "data" / "bird_counts.csv"
OUTPUTS = HERE / "outputs"

COLOURS = {"restored": "#2a7f62", "unrestored": "grey"}


def plot_sites(summary):
    fig, ax = plt.subplots()
    ax.bar(
        summary["site"],
        summary["mean_count"],
        color=summary["treatment"].map(COLOURS),
    )
    ax.set_xlabel("Site")
    ax.set_ylabel("Mean count per visit")
    return fig


def main():
    counts = load_counts(DATA)
    summary = summarise_sites(counts)
    print(summary)

    OUTPUTS.mkdir(exist_ok=True)
    fig = plot_sites(summary)
    fig.savefig(OUTPUTS / "site_means.png", dpi=150)


if __name__ == "__main__":
    main()
