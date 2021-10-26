from django.urls import path
from core.views import HomepageView

urlpatterns = [
    path("", HomepageView.as_view(), name="home"),
]
