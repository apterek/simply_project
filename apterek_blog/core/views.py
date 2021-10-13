from django.shortcuts import render
from django.http import HttpResponse
from core.models import Post, Tag


def index(request):
    posts = Post.objects.all().filter(tags=4)
    return render(request, "homepage.html", {"post": posts})
