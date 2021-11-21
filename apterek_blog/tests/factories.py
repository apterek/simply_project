import factory
import datetime
from factory.django import DjangoModelFactory
from core.models import Post, Categories
from django.contrib.auth.models import User


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Categories

    category = factory.Sequence(lambda n: f"Category-{n}")
    sub_category = factory.Sequence(lambda n: f"Category-{n}")


class UserFactory(DjangoModelFactory):
    def __init__(self, password):
        self.password = password

    class Meta:
        model = User
        django_get_or_create = ('username', 'email', 'password',)

    username = 'apterek-test'
    email = 'apterek-test@mail.ru'
    password = '12345678'


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Sequence(lambda n: f"Post-{n}")
    category = factory.SubFactory(CategoryFactory)
    content = factory.Sequence(lambda n: f"Content-{n}")
    author = factory.SubFactory(UserFactory)
    post_image = ""
    created_at = datetime.datetime.now()
    is_published = True
