import pandas as pd
from datetime import datetime

def load_ticket_data(path):
    df = pd.read_excel(path)

    # Normalize column names
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # Convert dates
    df["created"] = pd.to_datetime(df["created"], errors="coerce")
    df["updated"] = pd.to_datetime(df["updated"], errors="coerce")

    return df
