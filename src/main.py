import sqlite3
import pandas as pd
from pathlib import Path

# Create folder data
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

# Connect to SQLite
db_path = data_dir / "local.db"
conn = sqlite3.connect(db_path)

# -------------------------
# 1. Create tables
# -------------------------
conn.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
)
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    amount REAL,
    date TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

# -------------------------
# 2. Insert data
# -------------------------
conn.execute("DELETE FROM users")
conn.execute("DELETE FROM orders")

users = [
    (1, "Alice", "alice@example.com"),
    (2, "Bob", "bob@example.com"),
    (3, "Charlie", "charlie@example.com")
]

orders = [
    (1, 1, 100.0, "2025-09-10"),
    (2, 1, 50.0, "2025-09-11"),
    (3, 2, 75.0, "2025-09-10"),
    (4, 3, 200.0, "2025-09-12"),
    (5, 3, 150.0, "2025-09-12")
]

conn.executemany("INSERT INTO users VALUES (?, ?, ?)", users)
conn.executemany("INSERT INTO orders VALUES (?, ?, ?, ?)", orders)
conn.commit()

# -------------------------
# 3. SQL-запросы для отчета
# -------------------------
queries = {
    "orders_per_user": """
        SELECT u.name, COUNT(o.id) AS total_orders, SUM(o.amount) AS total_amount
        FROM users u
        LEFT JOIN orders o ON u.id = o.user_id
        GROUP BY u.name
        ORDER BY total_orders DESC
    """,
    "average_order_per_day": """
        SELECT date, AVG(amount) AS avg_amount, SUM(amount) AS total_amount
        FROM orders
        GROUP BY date
        ORDER BY date
    """
}

# -------------------------
# 4. Generation CSV reports
# -------------------------
report_dir = Path(".")
for name, query in queries.items():
    df = pd.read_sql_query(query, conn)
    csv_path = report_dir / f"{name}.csv"
    df.to_csv(csv_path, index=False)
    print(f"Report saved: {csv_path}")

# Close connection with db
conn.close()
print("ETL process ended.")







