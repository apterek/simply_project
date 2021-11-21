from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models


class TopologyImages(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile_name")
    image = models.ForeignKey("ImageModel",  on_delete=models.CASCADE, related_name="images_svg", blank=True, null=True)


class ImageModel(models.Model):
    topology_image = models.ImageField(upload_to='network_topology/%Y/%m/%d/', blank=True, null=True)
