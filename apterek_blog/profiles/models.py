from django.conf import settings
from django.db import models
from core.models import Post


GENDER_SETTING = (("Female", "Female"), ("Male", "Male"), ("Rather not say", "Rather not say"))


class ProfileInformation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="user_info", on_delete=models.CASCADE, blank=True, null=True
    )
    name = models.CharField(max_length=50)
    bday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_SETTING, blank=True, null=True)
    about = models.TextField(max_length=2000, blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photo/%Y/%m/%d/', blank=True, null=True)
    status = models.CharField(max_length=40, null=True, blank=True, default="My status")

    class Meta:
        verbose_name = "Profile info"
        verbose_name_plural = "Profiles info"

    def __str__(self):
        return f"{self.name}"
