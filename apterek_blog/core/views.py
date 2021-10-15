from django.shortcuts import render
from django.http import HttpResponse
from core.models import Post, Tag
from core.services import take_a_three_best_post


def view_homepage(request):
    posts = Post.objects.all()
    best_post1, best_post2, best_post3 = take_a_three_best_post()
    return render(request, "homepage.html", {"post": posts,
                                             "best_post1": best_post1,
                                             "best_post2": best_post2,
                                             "best_post3": best_post3})
