from django.urls import path, register_converter
from rest_framework import routers
from . import views


class FloatConverter:
    regex = "[-]?\d+\.\d+"

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value).replace('-', '')


register_converter(FloatConverter, 'float')
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('<float:lat>/<float:lon>/', views.Zmanim_View, name='response')
    # path('<int:year>/<int:month>/<int:day>', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
