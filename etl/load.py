import os
from config.config import PROCESSED_PATH

def load(df):
    print(f"Saving {len(df)} rows to {PROCESSED_PATH}...")
    os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)
    print("✅ Save complete")

import zipfile
from datetime import datetime

def archive_output(file_path):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = f"data/processed/archive_{timestamp}.zip"
    with zipfile.ZipFile(zip_name, "w") as zipf:
        zipf.write(file_path, arcname="traffic_clean.csv")
    print(f"📦 Archived to {zip_name}")



