import pandas as pd

def transform(df):
    print("Transforming...")

    # Rename columns
    df = df.rename(columns={
        "acci_time": "incident_time",
        "acci_name": "location",
        "acci_x": "longitude",
        "acci_y": "latitude"
    })

    # Drop rows with missing coordinates
    df = df.dropna(subset=["latitude", "longitude"])

    # Convert timestamps
    df["incident_time"] = pd.to_datetime(df["incident_time"], errors="coerce")
    df = df.dropna(subset=["incident_time"])

    # Add severity column if missing
    if "severity" not in df.columns:
        df["severity"] = "Unknown"

    # Create summary
    top_locations = df["location"].value_counts().head(5)
    summary = {
        "total_rows": len(df),
        "start_time": df["incident_time"].min(),
        "end_time": df["incident_time"].max(),
        "most_common_location": top_locations.index[0] if not top_locations.empty else "N/A",
        "top_5_locations": top_locations.to_dict()
    }

    return df, summary





