from django.urls import path, include
from rest_framework import routers
from .views import ProviderViewSet


router = routers.DefaultRouter()
router.register(r"", ProviderViewSet, basename="providers")

urlpatterns = [
    path("", include(router.urls)),
]
