PYTHON := python
PIP := pip
SRC := src/main.py
REQ := requirements.txt
DB := data/local.db
REPORT := report.csv

# Файлы и директории
DATA_DIR := data
SRC_DIR := src

# Основные команды
.PHONY: all install run clean docker report

# По умолчанию
all: install run report

# Установка зависимостей
install:
	$(PIP) install -r $(REQ)

# Запуск ETL-процесса
run:
	$(PYTHON) $(SRC)

# Очистка базы данных и отчетов
clean:
	rm -f $(DB) $(REPORT)
	mkdir -p $(DATA_DIR)

# Создание отчета после выполнения ETL
report:
	$(PYTHON) $(SRC) --report

# Запуск проекта в Docker
docker:
	docker-compose up --build

# Полная пересборка
rebuild: clean install run report
