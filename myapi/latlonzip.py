from uszipcode import SearchEngine


def get_lat_lon_zip(code):
    search = SearchEngine()
    results = search.by_zipcode(code)
    res_dict = results.to_dict()
    lat, lon = res_dict['lat'], res_dict['lng']
    return lat, lon
