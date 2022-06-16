from rest_framework import status
from rest_framework.test import APITestCase

from mozio_transport_suppliers.users.models import CustomUser
from mozio_transport_suppliers.providers.models import *


class ProviderCreateListUpdateTest(APITestCase):
    def setUp(self):

        self.user_data = {
            "email": "njokosi@gmail.com",
            "password": "sha123456789",
            "first_name": "Njokosi",
            "last_name": "Kawunju",
        }
        self.user = CustomUser.objects.create_user(**self.user_data)
        self.user_object = CustomUser.objects.get(id=self.user.id)

        self.data = {
            "user": self.user.id,
            "name": "Njokosi Jones",
            "email": "njokosi@gmail.com",
            "currency": "$",
            "language": "en",
            "phone_number": "+255754555467",
        }

        self.test_data = {
            "user": self.user_object,
            "name": "Njokosi Jones",
            "email": "njokosi@gmail.com",
            "currency": "$",
            "language": "en",
            "phone_number": "+255754555467",
        }
        self.provider = Provider.objects.create(**self.test_data)
        # self.provider_object = Provider.objects.get(id=self.provider.user_id)

    def test_can_create_provider(self):
        response = self.client.post("/api/v1/providers/", self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_can_read_provider_list(self):
        response = self.client.get("/api/v1/providers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_can_read_provider_detail(self):
    #     response = self.client.get(f"/api/v1/providers/{self.provider.id}/")
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_can_update_user(self):
    #     response = self.client.put(
    #         "/api/v1/providers/" + str(self.provider.id) + "/", self.data
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(
    #         Provider.objects.get(pk=self.provider.id).email, "jones@gmail.com"
    #     )

    # def test_can_delete_user(self):
    #     response = self.client.delete("/api/v1/providers/" + str(self.user.id) + "/")
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
