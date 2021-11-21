from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey("Categories", on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="profiles")
    post_image = models.ImageField(upload_to='post_images/%Y/%m/%d/', blank=True, null=True)
    number_of_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_published = models.BooleanField(default=False)
    likes = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-id']

    def __str__(self):
        return f"{self.title} - {self.created_at}"


class Categories(models.Model):
    category = models.CharField(max_length=255)
    sub_category = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.category}/{self.sub_category}"


class Comments(models.Model):
    name = models.CharField(max_length=50, default="Noname")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey("self",
                               verbose_name="parent_comment",
                               on_delete=models.SET_NULL,
                               blank=True, null=True)
    posts = models.ForeignKey(Post,
                              related_name="comment",
                              on_delete=models.CASCADE,
                              verbose_name="comment_to_post",
                              default="")

    class Meta:
        verbose_name = "Comments"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"{self.created_at}"


class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True)
    posts = models.ManyToManyField(Post, related_name="tags", blank=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.title


class Subscribers(models.Model):
    email = models.EmailField(max_length=30, unique=True)
    auth = models.BooleanField(default=False)
    subscribe_date = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = "Subscribers"
        verbose_name_plural = "Subscribers"

    def __str__(self):
        return f"{self.email}"
