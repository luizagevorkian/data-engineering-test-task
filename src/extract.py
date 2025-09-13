import requests
import os
import json
from datetime import date

def extract_data():
    """
    1. Fetch data from a public REST API
    2. Save raw response to /data/raw/yyyy-mm-dd/response.json
    3. Return parsed JSON as Python object
    """
    url = "https://jsonplaceholder.typicode.com/posts"  
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    today = date.today().strftime("%Y-%m-%d")
    save_path = f"data/raw/{today}"
    os.makedirs(save_path, exist_ok=True)

    with open(f"{save_path}/response.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"[EXTRACT] Saved raw data to {save_path}/response.json")
    return data