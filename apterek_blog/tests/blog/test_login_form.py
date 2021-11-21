import pytest
from tests.factories import UserFactory
from django import urls
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
class TestRegistrationForm:

    def setup_method(self):
        self.client = Client()
        self.url = reverse("login")
        UserFactory.create()

    @pytest.fixture
    def form_data(self):
        return {"email": "apterek-test@mail.ru", "password": "123456789"}

    def test_form(self, form_data):
        form_url = urls.reverse("login")
        response = self.client.post(form_url, form_data)
        assert response.status_code == 200


