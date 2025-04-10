# main.py - FastAPI backend to fetch real-time news

from fastapi import FastAPI
import requests

app = FastAPI()

# Replace with actual API keys and URLs for your news sources
DEITAONE_API_URL = 'https://api.deitaone.com/latest'
FINANCIALJUICE_API_URL = 'https://financialjuice.com/api'
BENZINGA_API_URL = 'https://api.benzinga.com/news'

# Example of fetching data from a source
@app.get("/latest-news")
def get_latest_news():
    response_deitaone = requests.get(DEITAONE_API_URL)
    response_financialjuice = requests.get(FINANCIALJUICE_API_URL)
    response_benzinga = requests.get(BENZINGA_API_URL)

    news = {
        "deitaone": response_deitaone.json(),
        "financialjuice": response_financialjuice.json(),
        "benzinga": response_benzinga.json(),
    }

    return news

# Add any other endpoints you need, or additional processing
