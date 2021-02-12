import datetime
import dateutil.parser
import timezonefinder
import pytz
from tzwhere import tzwhere


def get_hours(sunrise, sunset, lat, lon):
    sunrise = dateutil.parser.parse(sunrise)
    sunset = dateutil.parser.parse(sunset)
    where_obj = tzwhere.tzwhere()
    tz = where_obj.tzNameAt(lat, lon)
    print(tz)
    tz_real = pytz.timezone(tz)

    sunrise = sunrise.replace(tzinfo=datetime.timezone.utc).astimezone(tz=tz_real)
    sunset = sunset.replace(tzinfo=datetime.timezone.utc).astimezone(tz=tz_real)
    min_72 = datetime.timedelta(minutes=72)
    vilna_day_len = sunset - sunrise
    daybreak = sunrise - min_72
    nightfall = sunset + min_72
    magen_day_len = nightfall - daybreak
    magen_hour_len = magen_day_len/12
    vilna_hour_len = vilna_day_len/12
    return magen_hour_len, vilna_hour_len, sunrise, sunset, daybreak, nightfall

