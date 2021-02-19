from .SunriseSunset import get_sunrise_sunset
from .HourMath import get_hours
from .ZmanimCalcs import calcs


def no_lat_lon_json(lat, lon, date=None):
    # if date is not gievn it is None
    final_output = {}
    # get sunrise sunset
    sunrise_gmt, sunset_gmt = get_sunrise_sunset(lat, lon, date=date)
    # get sunrise sunset daybreak nightfall and proportional hours
    magen_hour_len, vilna_hour_len, sunrise, sunset, daybreak, nightfall = get_hours(sunrise_gmt, sunset_gmt, lat, lon)
    # get each dict, one for magen one for vilna
    magen_output = calcs(magen_hour_len, daybreak, nightfall)
    vilna_output = calcs(vilna_hour_len, sunrise, sunset)
    final_output['daybreak'] = daybreak
    final_output['sunrise'] = sunrise
    final_output["magen"] = magen_output
    final_output["vilna"] = vilna_output
    final_output['sunset'] = sunset
    final_output['nightfall'] = nightfall
    # organize data into a more readable dictionary
    test = final_output.copy()
    # change datetime objects to more readable string format
    for opinion, times in test.items():
        if opinion == 'magen' or opinion == 'vilna':
            for time, datetime in times.items():
                times[time] = datetime.strftime("%m/%d/%Y, %I:%M:%S %p")
        else:
            final_output[opinion] = times.strftime("%m/%d/%Y, %I:%M:%S %p")
    return final_output


if __name__ == '__main__':
    print(no_lat_lon_json(51.5013562, -0.1249302))


