import sqlite3

def load_to_db(df, db_name="local.db"):
    """
    1. Connect to SQLite database (or create if not exists)
    2. Write DataFrame to table
    3. Close connection
    """
    conn = sqlite3.connect(db_name)
    df.to_sql("posts", conn, if_exists="replace", index=False)
    conn.close()
    print(f"[LOAD] Data loaded to {db_name} (table: posts)")
