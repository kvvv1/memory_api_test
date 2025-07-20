import os
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')


def supabase_get(endpoint, params=None):
    """
    Realiza uma requisição GET à Supabase REST API.
    endpoint: string (nome da tabela ou endpoint)
    params: dicionário de filtros (query params)
    """
    url = f"{SUPABASE_URL}/{endpoint}"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json"
    }
    query = urlencode(params or {}, doseq=True)
    full_url = f"{url}?{query}" if query else url
    try:
        response = requests.get(full_url, headers=headers, timeout=15)
        response.raise_for_status()
        return response.json(), 200
    except requests.RequestException as e:
        return {"error": str(e)}, 500 