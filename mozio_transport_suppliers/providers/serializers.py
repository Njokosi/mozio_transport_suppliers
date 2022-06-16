from rest_framework import serializers
from .models import Provider, ServiceArea


class ProviderSerializer(serializers.ModelSerializer):

    """
    Provider serializer to handle CRUD operations.
    """

    class Meta:
        model = Provider
        fields = (
            "user",
            "name",
            "email",
            "currency",
            "language",
            "phone_number",
        )


class ServiceAreaSerializer(serializers.ModelSerializer):
    """
    Service Area serializer to handle CRUD operations.
    """

    class Meta:
        model = ServiceArea
        fields = (
            "id",
            "provider",
            "name",
            "price",
            "geo_json",
        )
        read_only_fields = ("id",)
