from django.http import JsonResponse, HttpResponseRedirect
from .Main import no_lat_lon_json
from django.shortcuts import render
from .latlonzip import get_lat_lon_zip
from geopy.geocoders import Nominatim

# Create your views here.


def Zmanim_View(request, lat, lon):
    zmanim_dict = no_lat_lon_json(lat, lon)
    return JsonResponse(zmanim_dict, json_dumps_params={'indent': 2})


def homepage(request):
    return render(request, 'myapi/index.html')


def date_zmanim(request, date, lat, lon):
    zmanim_dict = no_lat_lon_json(lat, lon, date=date)
    return JsonResponse(zmanim_dict, json_dumps_params={'indent': 2})


def zmanim_with_code(request, code):
    lat, lon = get_lat_lon_zip(code)
    zmanim_dict = no_lat_lon_json(lat, lon)
    return JsonResponse(zmanim_dict, json_dumps_params={'indent': 2})


def date_zmanim_with_code(request, code, date):
    lat, lon = get_lat_lon_zip(code)
    zmanim_dict = no_lat_lon_json(lat, lon, date=date)
    return JsonResponse(zmanim_dict, json_dumps_params={'indent': 2})


def display_times(request, zmanim_dict):
    magen_dict = zmanim_dict['magen']
    vilna_dict = zmanim_dict['vilna']
    return render(request, 'myapi/test.html', {
        'daybreak': zmanim_dict['daybreak'],
        'sunrise': zmanim_dict['sunrise'],
        'magen_sof_zman_kriyat_shema': magen_dict['sof_zman_kriyat_shema'],
        'magen_sof_zman_tefillah': magen_dict['sof_zman_tefilah'],
        'hazot': magen_dict['hazot'],
        'magen_minha_gedola': magen_dict['minha_gedola'],
        'magen_minha_ketana': magen_dict['minha_ketana'],
        'magen_plag_minha': magen_dict['plag_haminha'],
        'vilna_sof_zman_kriyat_shema': vilna_dict['sof_zman_kriyat_shema'],
        'vilna_sof_zman_tefillah': vilna_dict['sof_zman_tefilah'],
        'hazot': vilna_dict['hazot'],
        'vilna_minha_gedola': vilna_dict['minha_gedola'],
        'vilna_minha_ketana': vilna_dict['minha_ketana'],
        'vilna_plag_minha': vilna_dict['plag_haminha'],
        'sunset': zmanim_dict['sunset'],
        'nightfall': zmanim_dict['nightfall']
    })


def date_zmanim_fancy(request, date, lat, lon):
    zmanim_dict = no_lat_lon_json(lat, lon, date=date)
    return display_times(request, zmanim_dict)


def zmanim_with_code_fancy(request, code):
    lat, lon = get_lat_lon_zip(code)
    zmanim_dict = no_lat_lon_json(lat, lon)
    return display_times(request, zmanim_dict)


def date_zmanim_with_code_fancy(request, code, date):
    lat, lon = get_lat_lon_zip(code)
    zmanim_dict = no_lat_lon_json(lat, lon, date=date)
    return display_times(request, zmanim_dict)


def Zmanim_View_fancy(request, lat, lon):
    zmanim_dict = no_lat_lon_json(lat, lon)
    return display_times(request, zmanim_dict)


def search(request):
    if request.method == 'GET':
        return render(request, 'myapi/search.html')
    else:
        q = request.POST
        date = q.get('date')
        zip_code = q.get('zip_code')
        if zip_code == '':
            city = q.get('city')
            geo = Nominatim(user_agent='ZmanimAPI')
            location = geo.geocode(city)
            lat = location.latitude
            lon = location.longitude
            return HttpResponseRedirect(f"/{lat}/{lon}/{date}")
        return HttpResponseRedirect(f"us/{zip_code}/{date}")
