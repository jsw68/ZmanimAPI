from django.urls import path, register_converter
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


class FloatConverter:
    regex = r"[-]?\d+\.\d+"

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)


class DateConverter:
    regex = r'\d{4}[-]\d{2}[-]\d{2}'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value


class ZipConverter:
    regex = r'\d{5}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return value


register_converter(ZipConverter, 'zip')
register_converter(FloatConverter, 'float')
register_converter(DateConverter, 'date')
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('api/<float:lat>/<float:lon>/', views.Zmanim_View, name='lat_lon'),
    path('api/<float:lat>/<float:lon>/<date:date>/', views.date_zmanim, name="lat_lon_date"),
    path('api/us/<zip:code>/', views.zmanim_with_code, name="zip"),
    path('api/us/<zip:code>/<date:date>/', views.date_zmanim_with_code, name="zip_date"),
    path('<float:lat>/<float:lon>/', views.Zmanim_View_fancy, name='lat_lon_view'),
    path('<float:lat>/<float:lon>/<date:date>/', views.date_zmanim_fancy, name="lat_lon_date_view"),
    path('us/<zip:code>/', views.zmanim_with_code_fancy, name="zip_view"),
    path('us/<zip:code>/<date:date>/', views.date_zmanim_with_code_fancy, name="zip_date_view"),
    # path('<int:year>/<int:month>/<int:day>', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + staticfiles_urlpatterns()
