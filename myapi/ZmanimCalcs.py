import datetime


def calcs(hour, sunrise, sunset):
    output = {}
    # even though it is called hour, it is actually a proportional hour
    # even thought hey are called sunrise and sunset, they are passed nightfall adn daybreak for magen avraham
    three_hours = hour * 3
    two_hours = hour * 2
    # shema is three hours after sunrise
    sof_zman_kriyat_shema = sunrise + three_hours
    output["sof_zman_kriyat_shema"] = sof_zman_kriyat_shema
    sof_zman_tefilah = sof_zman_kriyat_shema + hour
    # 4 hours after sunrise
    output["sof_zman_tefilah"] = sof_zman_tefilah
    # six hours after sunrise
    hazot = sof_zman_tefilah + two_hours
    output["hazot"] = hazot
    half_hour = hour/2
    # half hour after midday
    minha_gedola = hazot + half_hour
    output["minha_gedola"] = minha_gedola
    # 2 and a half hours after midday
    minha_ketana = hazot + two_hours + half_hour
    output["minha_ketana"] = minha_ketana
    quarter_hour = hour/4
    # 1 and a quarter hour before sunset
    plag_haminha = sunset - hour - quarter_hour
    output["plag_haminha"] = plag_haminha
    # time_string = plag_haminha.strftime("%a %d %B %Y %H %p %M %S %F %Z")
    # print(time_string, hour, sunset, quarter_hour)
    return output
