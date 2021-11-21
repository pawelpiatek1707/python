import requests

api_endpoint = 'https://api.openbrewerydb.org/breweries'


class Brawery:
    def __init__(self, id: int, name: str, brewery_type: str, street: str, address_2: str, address_3: str, city: str, state: str, county_province: str, postal_code: str, country: str, longitude: str, latitude: str, phone: str, website_url: str, updated_at: str, created_at: str) -> None:
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state = state
        self.county_province = county_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.updated_at = updated_at
        self.created_at = created_at

    def __str__(self) -> str:
        return f"Brewery {self.name} located on {self.street} streed in {self.city}. Contact phone number: {self.phone}"


def fetch_data(endpoint: str) -> list:
    breweries_list = requests.get(endpoint).json()
    trimed_list = breweries_list[:20]
    breweries_obj_list = list()

    for brewery in trimed_list:
        breweries_obj_list.append(Brawery(brewery['id'], brewery['name'], brewery['brewery_type'], brewery['street'], brewery['address_2'], brewery['address_3'], brewery['city'], brewery['state'],
                                          brewery['county_province'], brewery['postal_code'], brewery['country'], brewery['longitude'], brewery['latitude'], brewery['phone'], brewery['website_url'], brewery['updated_at'], brewery['created_at']))

    return breweries_obj_list


try:
    fetched_breweries = fetch_data(api_endpoint)
    for brewery in fetched_breweries:
        print(brewery)
except requests.exceptions.RequestException as e:
    raise SystemExit(e)
