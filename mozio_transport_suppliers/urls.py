from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# This function attempts to import an admin module in each installed application.
admin.autodiscover()

schema_view = get_schema_view(
    openapi.Info(
        title="Mozio Transport Suppliers API",
        default_version="v1",
        description="API documentation for Mozio Transport Suppliers portal",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="njokosi@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
    path("api/v1/", include("mozio_transport_suppliers.users.urls")),  # social login
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/auth/", include("dj_rest_auth.urls")),  # authentication
    path("api/v1/auth/register/", include("dj_rest_auth.registration.urls")),
    # Local application API urls
    path("api/v1/providers/", include("mozio_transport_suppliers.providers.urls")),
    # Documentation
    path(
        "documentation/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]


admin.site.site_header = "Mozio Transport Suppliers Admin"
admin.site.site_title = "Mozio Transport Suppliers Admin Portal"
admin.site.index_title = "Welcome to Mozio Transport Suppliers Administration"
