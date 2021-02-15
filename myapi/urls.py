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
    regex = r'\d{4}[-/]\d{2}[-/]\d{2}'

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
    path('<float:lat>/<float:lon>/', views.Zmanim_View, name='response'),
    path('<float:lat>/<float:lon>/<date:date>/', views.date_zmanim, name="date_response"),
    path('us/<zip:code>/', views.zmanim_with_code, name="zmanim_zip"),
    path('us/<zip:code>/<date:date>/', views.date_zmanim_with_code, name="zmanim_zip_date")
    # path('<int:year>/<int:month>/<int:day>', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + staticfiles_urlpatterns()
