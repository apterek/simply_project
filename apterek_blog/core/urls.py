from django.urls import path
from django.conf import settings
from core.views import HomepageView, AboutView, PostDetailView, RegistrUser, SingInUser

urlpatterns = [
    path("", HomepageView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("registering/", RegistrUser.as_view(), name="registering"),
    path("login/", SingInUser.as_view(), name="login"),

    path("<str:post_title>/", PostDetailView.as_view(), name="post_detail"),  # always last
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
