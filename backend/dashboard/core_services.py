import os
import requests
import pandas as pd
import logging
import time
from typing import Optional
from requests.exceptions import RequestException

# ⛓️ Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")

# 🎯 Config fixo para ambiente local (sem .env)
API_URL = os.getenv("API_URL")
if not API_URL:
    API_URL = "http://127.0.0.1:8000"
API_URL = API_URL.rstrip("/")

# Retry config
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds


def _retry_request(method, url, headers=None, data=None, retries=MAX_RETRIES):
    for attempt in range(retries):
        try:
            if method == "POST":
                response = requests.post(url, data=data, headers=headers)
            else:
                response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response
        except RequestException as e:
            logging.warning(f"⚠️ Tentativa {attempt + 1}/{retries} falhou: {e}")
            time.sleep(RETRY_DELAY)
    raise Exception(f"🔥 Todas as tentativas falharam ao acessar {url}")


def fetch_kpis(token: str) -> dict:
    url = f"{API_URL}/kpi"
    headers = {"Authorization": f"Bearer {token}"}

    logging.info("📊 Buscando KPIs...")
    response = _retry_request("GET", url, headers=headers)
    return response.json()


def fetch_etl_data(token: str, limit: Optional[int] = 100) -> pd.DataFrame:
    url = f"{API_URL}/etl-data?limit={limit}"
    headers = {"Authorization": f"Bearer {token}"}

    logging.info(f"📁 Buscando dados ETL (limite={limit})...")
    response = _retry_request("GET", url, headers=headers)
    data = response.json()

    # 🚀🔧 Adição para evitar erros caso backend retorne dict de escalares:
    if isinstance(data, dict):
        data = [data]

    return pd.DataFrame(data)
