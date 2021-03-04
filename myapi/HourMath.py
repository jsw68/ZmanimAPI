import datetime
import dateutil.parser
import pytz
from tzwhere import tzwhere


def get_hours(sunrise, sunset, lat, lon):
    """Function to get the length of a proportional_hour when given the latitude, longitude, sunrise, and sunset."""
    # change sunrise sunset to datetime
    sunrise = dateutil.parser.parse(sunrise)
    sunset = dateutil.parser.parse(sunset)
    # instantiate tzwhere obj
    where_obj = tzwhere.tzwhere()
    # get the timezone at specifed coordinate
    tz = where_obj.tzNameAt(lat, lon)
    # change time zone obj to timezone string
    tz_real = pytz.timezone(tz)
    # make sunrise and sunset timezone aware
    sunrise = sunrise.replace(tzinfo=datetime.timezone.utc).astimezone(tz=tz_real)
    sunset = sunset.replace(tzinfo=datetime.timezone.utc).astimezone(tz=tz_real)
    # 72 minutes
    min_72 = datetime.timedelta(minutes=72)
    # get time between sunrise and sunset
    vilna_day_len = sunset - sunrise
    # calculate daybreak and nightfall
    daybreak = sunrise - min_72
    nightfall = sunset + min_72
    # get time between daybreak and nightfall
    magen_day_len = nightfall - daybreak
    # get the length of a proportional hour
    magen_hour_len = magen_day_len/12
    vilna_hour_len = vilna_day_len/12
    # return all times, but instead of as strings, this time in datetime format
    return magen_hour_len, vilna_hour_len, sunrise, sunset, daybreak, nightfall

