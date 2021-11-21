from rest_framework.test import APIClient
from rest_framework import status
import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestRegisterApi:
    def setup_method(self):
        self.client = APIClient()

    def test_user_api(self):
        response = self.client.post(reverse("api:login-list"),
                                    {
                                        "username": "testapi",
                                        "password": "api123api123"
                                    })
        assert response.status_code == status.HTTP_404_NOT_FOUND

        response = self.client.post(reverse("api:register-list"),
                                    {
                                        "username": "testapi",
                                        "email": "testapi@api.ap",
                                        "password": "api123api123"
                                    })
        assert response.status_code == status.HTTP_201_CREATED

        response = self.client.post(reverse("api:login-list"),
                                    {
                                        "username": "testapi",
                                        "password": "api123api123"
                                    })
        assert response.status_code == status.HTTP_404_NOT_FOUND

        response = self.client.post(reverse("api:logout-list"),
                                    {
                                        "username": "testapi",
                                        "password": "api123api123"
                                    })
        assert response.status_code == status.HTTP_200_OK
