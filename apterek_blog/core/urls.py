from django.urls import path
from core.views import HomepageView, AboutView

urlpatterns = [
    path("", HomepageView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about")
]
