import os
import csv
from datetime import datetime

def export_summary(summary):
    os.makedirs("data/summary", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    summary_path = os.path.join("data", "summary", f"summary_{timestamp}.csv")
    with open(summary_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Metric", "Value"])
        writer.writerow(["Total Rows", summary["total_rows"]])
        writer.writerow(["Start Time", summary["start_time"]])
        writer.writerow(["End Time", summary["end_time"]])
        writer.writerow(["Most Common Location", summary["most_common_location"]])
        writer.writerow([])
        writer.writerow(["Top 5 Locations"])
        for loc, count in summary["top_5_locations"].items():
            writer.writerow([loc, count])
    print(f"📊 Summary exported to {summary_path}")
    return summary_path
