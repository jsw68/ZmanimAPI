import requests
import json
import datetime
import dateutil.parser


def get_sunrise_sunset(lat, lon, date=None):
    """Function to get sunrise and sunset times for the given lat and lon and optional date"""
    # optional date paramater, if there is no date, it uses today
    # base url
    url = 'https://api.sunrise-sunset.org/json'
    # give it lat, lon
    # if there is no date, the API automatically uses today
    # formatted is 0 bec that gives it in an easier form to parse into datetime
    data = {
        'lat': lat,
        'lng': lon,
        'date': date,
        'formatted': 0
    }
    # get res using params
    response = requests.get(url, params=data)
    # make sure status code is ok
    response.raise_for_status()
    # change to dict
    res_dict = json.loads(response.text)
    # get results from dict
    results = res_dict['results']
    # get sunrise and sunrise, by default in GMT
    sunrise_GMT = results['sunrise']
    sunset_GMT = results['sunset']
    return sunrise_GMT, sunset_GMT
