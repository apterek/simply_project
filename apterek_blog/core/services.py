from django.db.models import QuerySet
from core.models import Post, Subscribers
import datetime


def take_a_three_best_post() -> QuerySet:
    best_posts = Post.objects.order_by("likes")[0:3]
    return best_posts


def create_new_subscribe(email: str, auth: bool = False) -> None:
    Subscribers.objects.create(email=email, auth=auth, subscribe_date=datetime.datetime.now())


def search_post(searching_string: str) -> QuerySet:
    find_posts = Post.objects.filter(title__icontains=searching_string)
    if not find_posts:
        find_posts = Post.objects.order_by("created_at")[0:3]
    return find_posts
