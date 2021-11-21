import pytest
from django.contrib.auth.models import User
from django import urls


@pytest.mark.django_db
class TestRegistrationForm:

    @pytest.fixture
    def form_data(self):
        return {"email": "apterek1@test.ru", "password": "123456789",
                "confirm_password": "123456789", "subscribe_check": "True"}

    @pytest.fixture
    def invalid_form_data(self):
        return {"email": "apterek1@test.ru", "password": "1213123123121",
                "confirm_password": "asdfsafsdf", "subscribe_check": "True"}

    def test_form(self, client, form_data, invalid_form_data):
        form_url = urls.reverse("registering")
        response_1 = client.post(form_url, form_data)
        response_2 = client.post(form_url, invalid_form_data)
        assert response_1.status_code == 302
        assert User.objects.all().last().email == "apterek1@test.ru"
        assert response_2.status_code == 200
