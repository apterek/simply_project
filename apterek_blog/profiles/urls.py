from django.urls import path
from profiles.views import ProfileView, UpdateProfile

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile_url"),
    path("update_profile/", UpdateProfile.as_view(), name="update_profile")
]

