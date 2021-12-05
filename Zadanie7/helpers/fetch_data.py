
import requests

from  models.Brawery import Brawery

def fetch_data(endpoint: str) -> list:
    breweries_list = requests.get(endpoint).json()
    trimed_list = breweries_list[:20]
    breweries_obj_list = list()

    for brewery in trimed_list:
        breweries_obj_list.append(
            Brawery(brewery['id'],
                    brewery['name'],
                    brewery['brewery_type'],
                    brewery['street'],
                    brewery['address_2'],
                    brewery['address_3'],
                    brewery['city'],
                    brewery['state'],
                    brewery['county_province'],
                    brewery['postal_code'],
                    brewery['country'],
                    brewery['longitude'],
                    brewery['latitude'],
                    brewery['phone'],
                    brewery['website_url'],
                    brewery['updated_at'],
                    brewery['created_at'])
        )

    return breweries_obj_list
