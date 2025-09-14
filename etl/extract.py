import pandas as pd
from config.config import RAW_DATA_PATH

def extract():
    print(f"Extracting from {RAW_DATA_PATH}")
    df = pd.read_csv(RAW_DATA_PATH)
    print("Columns found:", df.columns.tolist())
    return df

