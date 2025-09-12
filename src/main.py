from extract import extract_data
from transform import transform_data
from load import load_to_db
from analytics import run_queries
import pandas as pd
from sqlalchemy import create_engine
import json
from datetime import datetime


with open("data/raw/2025-09-12/response.json", "r") as f:
    raw_data = json.load(f)

df = pd.DataFrame(raw_data)

# 2. We process data
df = df[['id', 'title', 'body']]  # leave only the necessary fields
df = df.dropna()  # delete empty entries

# 3. connect to SQLite
engine = create_engine('sqlite:///data/local.db')

# 4. Save the DataFrame to the “posts” table
df.to_sql('posts', con=engine, if_exists='replace', index=False)

print("Данные успешно загружены в SQLite!")

if __name__ == "__main__":
    print("Starting mini ETL pipeline...")
    raw = extract_data()
    processed_df = transform_data(raw)
    load_to_db(processed_df)
    report = run_queries()
    print("Pipeline completed successfully!")
    print("Analytics Results:", report)

