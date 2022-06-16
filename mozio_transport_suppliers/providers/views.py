from django.shortcuts import render
from rest_framework import viewsets, mixins, permissions, status
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

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

    # TODO: We can also add permission classes
    # def get_permissions(self):
    #     """
    #     Instantiates and returns the list of permissions that provider view requires.

    #     - If user is admin return all the list of providers.
    #     """
    #     if self.action == "list":
    #         permission_classes = [permissions.IsAdminUser]
    #     else:
    #         permission_classes = [IsOwner]
    #     return [permission() for permission in permission_classes]


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


class SearchServiceAreaPolygonsApiView(APIView):
    """
    API endpoint that  outputs the all the polygon information associated with
    a particular latitude and longtitude
    """

    renderer_classes = [JSONRenderer]

    def get(self, request, *args, **kwargs):

        latitude = kwargs.get("lat")
        longitude = kwargs.get("long")

        if latitude is None or longitude is None:
            content = {"error": "Latitude and longitude are required"}
            Response(content, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            print("Hi there", latitude, longitude)
        content = {"success": "Response OK"}
        return Response(content, status=status.HTTP_200_OK)
