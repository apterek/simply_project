from django.urls import path
from django.conf import settings
from core.views import HomepageView, AboutView, RegistrUser, success_registration,\
    PostDetailView, login_user, logout_user

urlpatterns = [
    path("", HomepageView.as_view(), name="home"),
    path("posts_<str:category>/", HomepageView.as_view(), name="home_with_category"),
    path("about/", AboutView.as_view(), name="about"),
    path("registering/", RegistrUser.as_view(), name="registering"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("success/", success_registration, name="success_registration"),
    path("<str:post_title>/", PostDetailView.as_view(), name="post_detail"),
]

