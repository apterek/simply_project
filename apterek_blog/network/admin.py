from django.contrib import admin
from network.models import TopologyImages, ImageModel


@admin.register(TopologyImages)
class TopologyImagesAdmin(admin.ModelAdmin):
    list_display = ("username", "image",)
    search_fields = ("username", "image", )


@admin.register(ImageModel)
class TopologyImagesAdmin(admin.ModelAdmin):
    list_display = ("topology_image", )
    search_fields = ("topology_image", )

