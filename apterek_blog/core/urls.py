from django.urls import path
from core.views import view_homepage

urlpatterns = [
    path("", view_homepage, name="home"),
]
