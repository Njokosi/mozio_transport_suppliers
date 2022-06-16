from rest_framework import status
from rest_framework.test import APITestCase

from mozio_transport_suppliers.users.models import CustomUser
from mozio_transport_suppliers.providers.models import *


class CreateServiceAreaTest(APITestCase):
    def setUp(self):
        self.user_data = {
            "email": "njokosi@gmail.com",
            "password": "sha123456789",
            "first_name": "Njokosi",
            "last_name": "Kawunju",
        }
        self.user = CustomUser.objects.create_user(**self.user_data)
        
        self.provider_data = {
            "user_id": self.user.id,
            "name": "Njokosi Jones",
            "email": "njokosi@gmail.com",
            "currency": "$",
            "language": "en",
            "phone_number": "+255754555467",
        }
        self.provider = Provider.objects.create(**self.provider_data)
        
        
        self.service_area_data = {
            "name": "Test area 1",
            "price": "1000.53",
            "provider": self.provider.user.id,
            "geo_json": "data",
        }

    def test_can_create_service_area(self):
        response = self.client.post(
            "/api/v1/providers/service-areas/", self.service_area_data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


