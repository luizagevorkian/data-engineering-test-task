from extract import extract_data
from transform import transform_data
from load import load_to_db
from analytics import run_queries

if __name__ == "__main__":
    print("Starting mini ETL pipeline...")
    raw = extract_data()
    processed_df = transform_data(raw)
    load_to_db(processed_df)
    report = run_queries()
    print("Pipeline completed successfully!")
    print("Analytics Results:", report)
