from django.urls import path, include, register_converter
from rest_framework import routers
from .views import ProviderViewSet, ServiceAreaViewSet, SearchServiceAreaPolygonsApiView

from mozio_transport_suppliers.converters import FloatUrlParameterConverter

register_converter(FloatUrlParameterConverter, "float")

router = routers.DefaultRouter()

router.register(r"service-areas", ServiceAreaViewSet, basename="provider-service-areas")
router.register(r"", ProviderViewSet, basename="providers")

urlpatterns = [
    path(
        "service-areas/search-polygons/lat=<float:lat>/&long=<float:long>/",
        SearchServiceAreaPolygonsApiView.as_view(),
        name="search-polygons",
    ),
    path("", include(router.urls)),
]
