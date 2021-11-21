from django.urls import include, path
from rest_framework import routers
from api.user.views import RegisterViewSet, LoginView, LogoutView

app_name = "api"

router = routers.DefaultRouter()
router.register(r"register", RegisterViewSet, "register")
router.register(r"login", LoginView, "login")
router.register(r"logout", LogoutView, "logout")

urlpatterns = [
    path("", include(router.urls)),
]