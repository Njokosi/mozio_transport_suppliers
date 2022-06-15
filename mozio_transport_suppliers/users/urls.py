from django.urls import path, include
from mozio_transport_suppliers.users.views import GoogleLoginView

urlpatterns = [
    path("social/login/google/", GoogleLoginView.as_view(), name="google"),
]
