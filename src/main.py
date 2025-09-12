from extract import extract_data
from transform import transform_data
from load import load_to_db
from analytics import run_queries
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    print(" Starting mini ETL pipeline...")

    # 1. Extract
    raw = extract_data()

    # 2. Transform
    processed_df = transform_data(raw)

    # 3. Load
    load_to_db(processed_df)

    # 4. Analytics
    report = run_queries()

    print("Pipeline completed successfully!")
    print("Analytics Results:", report)
