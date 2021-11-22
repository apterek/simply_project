from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/", include("api.urls", namespace="api",)),
    path("django-rq/", include("django_rq.urls")),
    path('admin/', admin.site.urls),
    path('api-auth/', include("rest_framework.urls")),
    path('profile/', include("profiles.urls")),
    path('network_utils/', include("network.urls")),
    path('', include("core.urls")),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
