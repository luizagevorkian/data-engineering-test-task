# data-engineering-test-task
Data Engineer Test Task
# Mini Data Engineering Pipeline

## Описание
This project implements a simple ETL process.:
1. **Extract** — loads data from the public REST API.
2. **Transform** — cleans and enriches the data.
3. **Load** — loads it into SQLite.
4. **Analytics** — executes SQL queries and saves the report.

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
