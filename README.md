# data-engineering-test-task
Data Engineer Test Task
# Mini Data Engineering Pipeline

## Описание
Этот проект реализует простой ETL-процесс:
1. **Extract** — загружает данные из публичного REST API.
2. **Transform** — очищает и обогащает данные.
3. **Load** — загружает их в SQLite.
4. **Analytics** — выполняет SQL-запросы и сохраняет отчет.

---

## Установка и запуск
```bash
pip install -r requirements.txt
python src/main.py
