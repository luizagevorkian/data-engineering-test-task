import pandas as pd
import os
from datetime import date

def transform_data(raw_data):
    """
    1. Convert raw JSON to pandas DataFrame
    2. Select only needed fields
    3. Rename fields if necessary
    4. Clean invalid values / add calculated field
    5. Save processed data to /data/processed/yyyy-mm-dd/data.parquet
    6. Return cleaned DataFrame
    """
    df = pd.DataFrame(raw_data)

    # filtering and conversion
    if "userId" in df.columns:
        df = df[['userId', 'id', 'title', 'body']]
        df.rename(columns={'userId': 'user_id', 'id': 'post_id'}, inplace=True)

    # Add a calculated field
    if "title" in df.columns:
        df['title_length'] = df['title'].apply(len)

    today = date.today().strftime("%Y-%m-%d")
    save_path = f"data/processed/{today}"
    os.makedirs(save_path, exist_ok=True)

    parquet_path = f"{save_path}/data.parquet"
    df.to_parquet(parquet_path, index=False)
    print(f"[TRANSFORM] Saved processed data to {parquet_path}")

    return df





