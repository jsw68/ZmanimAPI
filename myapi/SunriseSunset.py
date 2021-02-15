import requests
import json
import datetime
import dateutil.parser


def get_sunrise_sunset(lat, lon, date=None):
    url = 'https://api.sunrise-sunset.org/json'
    # today = '2021-06-08'
    data = {
        'lat': lat,
        'lng': lon,
        'date': date,
        'formatted': 0
    }
    response = requests.get(url, params=data)
    response.raise_for_status()
    res_dict = json.loads(response.text)
    results = res_dict['results']
    sunrise_GMT = results['sunrise']
    sunset_GMT = results['sunset']
    return sunrise_GMT, sunset_GMT
