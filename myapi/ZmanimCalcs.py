import datetime


def calcs(proportional_hour, halachik_day_begins, halachik_day_ends):
    """Function to callculate the Zmanim for Magen Avraham and Vilna Gaon when given the length of a
    proportional hour and the time that the halachik day starts and ends"""
    output = {}
    # shema is three proportional_hours after halachik_day_begins
    sof_zman_kriyat_shema = halachik_day_begins + proportional_hour * 3
    output["sof_zman_kriyat_shema"] = sof_zman_kriyat_shema
    # 4 proportional_hours after halachik_day_begins
    sof_zman_tefilah = sof_zman_kriyat_shema + proportional_hour
    output["sof_zman_tefilah"] = sof_zman_tefilah
    # six proportional_hours after halachik_day_begins
    hazot = sof_zman_tefilah + proportional_hour * 2
    output["hazot"] = hazot
    # half proportional_hour after midday
    minha_gedola = hazot + proportional_hour/2
    output["minha_gedola"] = minha_gedola
    # 2 and a half proportional_hours after midday
    minha_ketana = hazot + proportional_hour * 2 + proportional_hour/2
    output["minha_ketana"] = minha_ketana
    # 1 and a quarter proportional_hour before halachik_day_ends
    plag_haminha = halachik_day_ends - proportional_hour - proportional_hour/4
    output["plag_haminha"] = plag_haminha
    return output
