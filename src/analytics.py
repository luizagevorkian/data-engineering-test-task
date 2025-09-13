import sqlite3
import pandas as pd

def run_queries(db_name="local.db"):
    """
    1. Connect to database
    2. Run SQL queries
    3. Save results to report.csv
    4. Return results as dictionary
    """
    conn = sqlite3.connect(db_name)

    queries = {
        "average_title_length": "SELECT AVG(title_length) AS avg_len FROM posts",
        "count_unique_users": "SELECT COUNT(DISTINCT user_id) AS users FROM posts",
        "posts_per_user": "SELECT user_id, COUNT(*) AS post_count FROM posts GROUP BY user_id"
    }

    results = {}
    for name, query in queries.items():
        df = pd.read_sql_query(query, conn)
        results[name] = df.to_dict(orient="records")

    pd.DataFrame(results["posts_per_user"]).to_csv("report.csv", index=False)
    print("[ANALYTICS] Report saved to report.csv")

    conn.close()
    return results












