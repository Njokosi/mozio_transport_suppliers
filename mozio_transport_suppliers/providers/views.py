from django.shortcuts import render
from rest_framework import viewsets, mixins, permissions

from mozio_transport_suppliers.users.permissions import IsOwner
from mozio_transport_suppliers.providers.models import Provider
from mozio_transport_suppliers.providers.serializers import ProviderSerializer


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
    Only admin will have permission to view list of all the providers.
    """

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    lookup_field = "user"

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that provider view requires.
        """
        if self.action == "list":
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]
