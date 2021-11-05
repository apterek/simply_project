from django.shortcuts import redirect, render
from core.models import Post
from core.services import take_a_three_best_post, create_new_subscribe, search_post
from core.forms import SubscriberForm, RegistrationForm, SignInForm
from django.views.generic import CreateView, TemplateView, FormView
from django.contrib import messages


class HomepageView(CreateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        search_query = self.request.GET.get("search_field", None)  # If the search form is submitted
        if search_query:
            posts = search_post(search_query)
        else:
            posts = Post.objects.all()
        best_post1, best_post2, best_post3 = take_a_three_best_post()
        form = SubscriberForm()
        return {"post": posts, "best_post1": best_post1,
                "best_post2": best_post2, "best_post3": best_post3, "form": form}

    def post(self, request, *args, **kwargs):
        subscribe_form = SubscriberForm(self.request.POST)
        if subscribe_form.is_valid() and self.request.user.is_authenticated:
            create_new_subscribe(subscribe_form.cleaned_data["email"], True)
            messages.info(self.request, "Thanks for subscribe!")
            return redirect("home")
        elif subscribe_form.is_valid():
            create_new_subscribe(subscribe_form.cleaned_data["email"])
            messages.info(self.request, "Thanks for subscribe!")
            return redirect("home")


class AboutView(TemplateView):
    template_name = "about/about.html"

    def get_context_data(self, **kwargs):
        posts = Post.objects.filter(pk=2)
        return {"posts": posts}


class PostDetailView(TemplateView):
    template_name = "core_posts/single_post.html"

    def get_context_data(self, **kwargs):
        post = Post.objects.get(title=kwargs["post_title"])
        return {"post": post}


class RegistrUser(FormView):
    template_name = "profile/sign_up.html"
    form_class = RegistrationForm
    success_url = "about"  # TEST VALUE !!!! CHANGE !!!

    def form_valid(self, form):
        return super().form_valid(form)


class SingInUser(FormView):
    template_name = "profile/sign_in.html"
    form_class = SignInForm
    success_url = "about"  # TEST VALUE !!!! CHANGE !!!

    def form_valid(self, form):
        return super().form_valid(form)
