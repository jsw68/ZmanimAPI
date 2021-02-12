import datetime
import dateutil.parser


def get_hours(sunrise, sunset):
    sunrise = dateutil.parser.parse(sunrise)
    sunset = dateutil.parser.parse(sunset)
    sunrise = sunrise.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)
    sunset = sunset.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)
    min_72 = datetime.timedelta(minutes=72)
    vilna_day_len = sunset - sunrise
    daybreak = sunrise - min_72
    nightfall = sunset + min_72
    magen_day_len = nightfall - daybreak
    magen_hour_len = magen_day_len/12
    vilna_hour_len = vilna_day_len/12
    return magen_hour_len, vilna_hour_len, sunrise, sunset, daybreak, nightfall

