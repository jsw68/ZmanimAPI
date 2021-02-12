from .LocationIQ import get_lat_lon
from .SunriseSunset import get_sunrise_sunset
from .HourMath import get_hours
from .ZmanimCalcs import calcs


def main():
    lat, lon = get_lat_lon()
    print(lat, lon)
    sunrise_gmt, sunset_gmt = get_sunrise_sunset(lat, lon)
    magen_hour_len, vilna_hour_len, sunrise, sunset, daybreak, nightfall = get_hours(sunrise_gmt, sunset_gmt)
    print(magen_hour_len, vilna_hour_len)
    print(calcs(magen_hour_len, sunrise, sunset))
    calcs(vilna_hour_len, sunrise, sunset)


def no_lat_lon_json(lat, lon):
    final_output = {}
    print(lat, lon)
    sunrise_gmt, sunset_gmt = get_sunrise_sunset(lat, lon)
    magen_hour_len, vilna_hour_len, sunrise, sunset, daybreak, nightfall = get_hours(sunrise_gmt, sunset_gmt, lat, lon)
    magen_output = calcs(magen_hour_len, sunrise, sunset)
    vilna_output = calcs(vilna_hour_len, sunrise, sunset)
    final_output['daybreak'] = daybreak
    final_output['sunrise'] = sunrise
    final_output["magen"] = magen_output
    final_output["vilna"] = vilna_output
    final_output['sunset'] = sunset
    final_output['nightfall'] = nightfall
    test = final_output.copy()
    for opinion in test.values():
        for time, datetime in opinion.items():
            opinion[time] = datetime.strftime("%m/%d/%Y, %H:%M:%S")
    return final_output


if __name__ == '__main__':
    print(no_lat_lon_json(51.5013562, -0.1249302))


