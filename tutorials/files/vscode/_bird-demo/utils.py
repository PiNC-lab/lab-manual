import pandas as pd


def load_counts(path):
    """Read the bird count data and drop visits with no count."""
    counts = pd.read_csv(path, parse_dates=["visit_date"])
    return counts.dropna(subset=["count"])


def summarise_sites(counts):
    """Mean count per visit for each site."""
    return (
        counts
        .groupby(["site", "treatment"], as_index=False)
        .agg(mean_count=("count", "mean"))
    )
