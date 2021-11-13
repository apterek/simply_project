from django.contrib import admin
from profiles.models import ProfileInformation


@admin.register(ProfileInformation)
class PostAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "bday", "gender", "post", "about", )
    search_fields = ("user", "name", "post", )

