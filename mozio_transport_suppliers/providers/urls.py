from django.urls import path, include
from rest_framework import routers
from .views import ProviderViewSet, ServiceAreaViewSet


router = routers.DefaultRouter()
router.register(r"", ProviderViewSet, basename="providers")
router.register(r"service-areas", ServiceAreaViewSet, basename="service-areas")

urlpatterns = [
    path("", include(router.urls)),
]
