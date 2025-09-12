# src/load.py
from sqlalchemy import create_engine
import os

def load_to_db(df, table_name="posts"):
    """
    Load processed data to a database using SQLAlchemy.
    DATABASE_URL читается из переменной окружения.
    
    Пример DATABASE_URL:
    - SQLite (локально): sqlite:///local.db
    - PostgreSQL (в Docker): postgresql+psycopg2://postgres:postgres@db:5432/postgres
    """
    db_url = os.getenv("DATABASE_URL", "sqlite:///local.db")
    engine = create_engine(db_url)

    try:
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        print(f"[LOAD] Data loaded to {db_url} (table: {table_name})")
    except Exception as e:
        print(f"[LOAD] Failed to load data: {e}")
