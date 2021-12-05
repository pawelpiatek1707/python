import requests
from helpers.fetch_data import fetch_data
from consts.api import api_endpoint

try:
    fetched_breweries = fetch_data(f"{api_endpoint}/breweries")
    for brewery in fetched_breweries:
        print(brewery)
except requests.exceptions.RequestException as e:
    raise SystemExit(e)
