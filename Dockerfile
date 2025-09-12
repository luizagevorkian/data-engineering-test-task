FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src ./src
COPY data ./data
ENV DATABASE_URL=postgresql+psycopg2://postgres:postgres@db:5432/postgres
CMD ["python", "src/main.py"]
