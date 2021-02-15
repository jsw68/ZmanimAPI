import datetime


def calcs(hour, sunrise, sunset):
    output = {}
    three_hours = hour * 3
    two_hours = hour * 2
    sof_zman_kriyat_shema = sunrise + three_hours
    output["sof_zman_kriyat_shema"] = sof_zman_kriyat_shema
    sof_zman_tefilah = sof_zman_kriyat_shema + hour
    output["sof_zman_tefilah"] = sof_zman_tefilah
    hazot = sof_zman_tefilah + two_hours
    output["hazot"] = hazot
    half_hour = hour/2
    minha_gedola = hazot + half_hour
    output["minha_gedola"] = minha_gedola
    minha_ketana = hazot + two_hours + half_hour
    output["minha_ketana"] = minha_ketana
    quarter_hour = hour/4
    plag_haminha = sunset - hour - quarter_hour
    output["plag_haminha"] = plag_haminha
    # time_string = sof_zman_tefilah.strftime("%a %d %B %Y %H %p %M %S %F %Z")
    return output

