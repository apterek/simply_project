from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    form = 1
    return render(request, "base.html")
