# data-engineering-test-task
Data Engineer Test Task
# Mini Data Engineering Pipeline

## Description
This project implements a simple ETL process.:
1. **Extract** — loads data from the public REST API.
2. **Transform** — cleans and enriches the data.
3. **Load** — loads it into SQLite.
4. **Analytics** — executes SQL queries and saves the report.

---

Implementation Steps
Step 1: Data Extraction

Used Python requests library to fetch posts from JSONPlaceholder API.

Raw API response saved locally in:

data/raw/yyyy-mm-dd/response.json

Step 2: Data Transformation

Loaded raw JSON using pandas.

Selected only relevant fields: userId, id, title, body.

Renamed columns for consistency if necessary.

Added a new field: title_length (calculated length of each post title).

Saved transformed data as CSV or Parquet in:

data/processed/yyyy-mm-dd/data.parquet

Step 3: Load into Database

Created SQLite database (local.db) and a table posts.

Loaded transformed data into the posts table using SQLAlchemy.

Step 4: Analytics

Ran SQL queries to generate basic insights:

Count of unique users.

Average title length.

Posts per user (grouped by userId).

Exported query results to CSV/JSON and included them in a PDF report.

---

## Installation and start-up
```bash
pip install -r requirements.txt
python src/main.py

Running via Docker

Build containers:

docker-compose build


Run pipeline:

docker-compose up

Running via Makefile
.PHONY: run
run:
    python src/main.py


Run:

make run
