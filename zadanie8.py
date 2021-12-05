import argparse
import requests
from Zadanie7.helpers.fetch_data import fetch_data
from Zadanie7.consts.api import api_endpoint as breweries_api

parser = argparse.ArgumentParser(description='Brewery city')

parser.add_argument('City', metavar='city', type=str)

args = parser.parse_args()

input_path = args.City

api_endpoint = f'{breweries_api}/breweries?by_city={input_path}'

try:
    fetched_breweries = fetch_data(api_endpoint)
    for brewery in fetched_breweries:
        print(brewery)
except requests.exceptions.RequestException as e:
    raise SystemExit(e)
