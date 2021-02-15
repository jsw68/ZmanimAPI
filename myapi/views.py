from django.http import JsonResponse
from .Main import no_lat_lon_json
from django.shortcuts import render
# Create your views here.


def Zmanim_View(request, lat, lon):
    zmanim_dict = no_lat_lon_json(lat, lon)
    # zmanim_json = json.loads(str(zmanim_dict))
    # json_response = json.dumps(zmanim_dict, indent=2)
    # response = json.loads(json_response)

    return JsonResponse(zmanim_dict, json_dumps_params={'indent': 2})


def homepage(request):
    return render(request, 'myapi/index.html')


def date_zmanim(request, date, lat, lon):
    zmanim_dict = no_lat_lon_json(lat, lon, date=date)
    return JsonResponse(zmanim_dict, json_dumps_params={'indent': 2})
