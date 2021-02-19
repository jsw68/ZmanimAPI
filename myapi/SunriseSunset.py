import requests
import json
import datetime
import dateutil.parser


def get_sunrise_sunset(lat, lon, date=None):
    # optional date paramater, if there is no date, it uses today
    url = 'https://api.sunrise-sunset.org/json'
    # today = '2021-06-08'
    data = {
        'lat': lat,
        'lng': lon,
        'date': date,
        'formatted': 0
    }
    # get sunrise sunset by lat lon
    # formatted is 0 bec that gives it in an easier form to parse into datetime
    response = requests.get(url, params=data)
    response.raise_for_status()
    res_dict = json.loads(response.text)
    results = res_dict['results']
    sunrise_GMT = results['sunrise']
    sunset_GMT = results['sunset']
    return sunrise_GMT, sunset_GMT
