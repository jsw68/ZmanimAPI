import pgeocode


def get_lat_lon_zip(code):
    nominatim = pgeocode.Nominatim('us')
    table = nominatim.query_postal_code(code)
    lat = table['latitude']
    lon = table['longitude']
    return lat, lon
