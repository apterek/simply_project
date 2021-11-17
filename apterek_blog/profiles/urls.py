from django.urls import path
from django.conf import settings
from profiles.views import ProfileView, UpdateProfile

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile_url"),
    path("update_profile/", UpdateProfile.as_view(), name="update_profile")
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)