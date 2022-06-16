from django.shortcuts import render
from rest_framework import viewsets, mixins, permissions

from mozio_transport_suppliers.users.permissions import IsOwner
from mozio_transport_suppliers.providers.models import Provider, ServiceArea
from mozio_transport_suppliers.providers.serializers import (
    ProviderSerializer,
    ServiceAreaSerializer,
)


class ProviderViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows providers to be viewed or edited.


    AUTHORIZATIONS:
        - Only admin will have permission to view list of all the providers.
        - The user in session can update the details of his provider profile
    """

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    lookup_field = "user"

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that provider view requires.

        - If user is admin return all the list of providers.
        """
        if self.action == "list":
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]


class ServiceAreaViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows service areas to be created, viewed or edited.
    """

    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
