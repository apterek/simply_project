from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, FormView, UpdateView, DetailView
from profiles.forms import EditProfileInfoForm


class ProfileView(TemplateView):



