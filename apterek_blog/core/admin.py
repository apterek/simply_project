from django.contrib import admin
from core.models import Post, Categories, Comments, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "author", "created_at",)
    search_fields = ("title", "author", "created_at", )
    readonly_fields = ("created_at", "number_of_views", )


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("category", "sub_category", )
    search_fields = ("category", "sub_category", )


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("posts", "created_at",)
    search_fields = ("posts", )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("title", )
    search_fields = ("posts", "title")
