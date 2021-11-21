import argparse
import requests
from zadanie7 import fetch_data

parser = argparse.ArgumentParser(description='Brewery city')

parser.add_argument('City', metavar='city', type=str)

args = parser.parse_args()

input_path = args.City

api_endpoint = f'https://api.openbrewerydb.org/breweries?by_city={input_path}'

try:
    fetched_breweries = fetch_data(api_endpoint)
    for brewery in fetched_breweries:
        print(brewery)
except requests.exceptions.RequestException as e:
    raise SystemExit(e)
