PYTHON := python
PIP := pip
SRC := src/main.py
REQ := requirements.txt
DB := data/local.db
REPORT := report.csv


DATA_DIR := data
SRC_DIR := src

.PHONY: all install run clean docker report

all: install run report

install:
	$(PIP) install -r $(REQ)

# ETL-process
run:
	$(PYTHON) $(SRC)

# Cleaning up the database and reports
clean:
	rm -f $(DB) $(REPORT)
	mkdir -p $(DATA_DIR)

# Creating a report after ETL execution
report:
	$(PYTHON) $(SRC) --report

# Launching a project in Docker
docker:
	docker-compose up --build

# Complete reassembly
rebuild: clean install run report
