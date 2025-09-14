import os
import matplotlib.pyplot as plt

def plot_top_locations(summary):
    os.makedirs("data/summary", exist_ok=True)
    locations = list(summary["top_5_locations"].keys())
    counts = list(summary["top_5_locations"].values())

    plt.figure(figsize=(10, 6))
    plt.barh(locations[::-1], counts[::-1], color="skyblue")
    plt.xlabel("Number of Incidents")
    plt.title("Top 5 Incident Locations")
    plt.tight_layout()

    out_path = os.path.join("data", "summary", "top_locations.png")
    plt.savefig(out_path)
    print(f"📈 Visualization saved to {out_path}")
    return out_path


