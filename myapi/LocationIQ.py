import requests
import json


def get_lat_lon(code):
    # gets latitude and longitude from a zip code
    url = "https://us1.locationiq.com/v1/search.php"

    data = {
        'key': 'pk.65b9351b2e107133b7d3ea99a3f181d7',
        'q': code,
        'countrycode': 'us',
        'format': 'json'
    }
    # get lat and lon from json response
    response = requests.get(url, params=data)
    response.raise_for_status()
    res_dict = json.loads(response.text)[0]
    lat = res_dict['lat']
    lon = res_dict['lon']
    return lat, lon
