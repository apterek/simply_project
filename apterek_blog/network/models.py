from django.conf import settings
from django.db import models


class TopologyImages(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile_name")
    topology_image = models.ImageField(upload_to='network_topology/%Y/%m/%d/')
