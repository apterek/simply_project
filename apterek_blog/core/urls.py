from base64 import encode

from django.urls import path
from core.views import HomepageView, AboutView, PostDetailView

urlpatterns = [
    path("", HomepageView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("<str:post_title>/", PostDetailView.as_view(), name="post_detail"),
]


encode