import pytest
from django.urls import reverse
from tests.factories import PostFactory
from django.test import Client
from core.models import Post, Subscribers
from django import urls


@pytest.mark.django_db
class TestMainPage:

    def setup_method(self):
        self.client = Client()
        self.url = reverse("home")
        PostFactory.create_batch(15)

    @pytest.fixture
    def form_data(self):
        return {"email": "apterek@test.ru"}

    def test_main_page_view(self):
        response = self.client.get(f"{self.url}")
        assert response.status_code == 200

    def test_paginations(self):
        test_page = ("page=1", "page=2", "page=3")
        for query in test_page:
            response = self.client.get(f"{self.url}?{query}")
            assert response.status_code == 200

    def test_categories_filter(self):
        test_filter = (
            "",
            "posts_network",
            "posts_system",
            "posts_virtualization",
            "posts_s&s"
        )
        for query in test_filter:
            response = self.client.get(f"{self.url}?{query}")
            assert response.status_code == 200
        
    def test_search(self):
        posts = Post.objects.all()
        for post in posts:
            title = post.title
            response = self.client.get(f"{self.url}?search_field={title}")
            assert response.status_code == 200

    def test_subscribe_form(self, client, form_data):
        form_url = urls.reverse("home")
        response = client.post(form_url, form_data)
        assert response.status_code == 302
        assert Subscribers.objects.all().last().email == "apterek@test.ru"
