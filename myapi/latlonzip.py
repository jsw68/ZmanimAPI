from uszipcode import SearchEngine


def get_lat_lon_zip(code):
    """Function that returns the latitude and longitude when given a US zip code"""
    # instantiate search obj
    search = SearchEngine()
    # search for the zip code given
    results = search.by_zipcode(code)
    # get results as a dict
    res_dict = results.to_dict()
    # find and return the lat lon coords for the zip code
    lat, lon = res_dict['lat'], res_dict['lng']
    return lat, lon
