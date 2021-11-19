from django.contrib.auth.models import User
from django.db.models import QuerySet
from core.models import Post, Subscribers
import datetime
import re


def take_a_three_best_post() -> QuerySet:
    best_posts = Post.objects.order_by("likes")[0:3]
    return best_posts


def create_username_from_email(email: str) -> str:
    regex = re.compile(r"(\S+)(@)")
    match = regex.match(email)
    if match:
        return match.group(1)


def create_user(email: str, password: str) -> None:
    username = create_username_from_email(email)
    User.objects.create_user(username=username, email=email, password=password)


def create_new_subscribe(email: str, auth: bool = False) -> None:
    Subscribers.objects.create(email=email, auth=auth, subscribe_date=datetime.datetime.now())


def search_post(searching_string: str) -> QuerySet:
    find_posts = Post.objects.filter(title__icontains=searching_string)
    if not find_posts:
        find_posts = Post.objects.order_by("created_at")[0:3]
    return find_posts

