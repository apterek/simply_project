from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from core.models import Post
from core.services import take_a_three_best_post, create_new_subscribe, search_post,\
    create_user, create_username_from_email
from core.forms import SubscriberForm, RegistrationForm, LoginForm
from django.views.generic import CreateView, TemplateView, FormView
from django.contrib import messages
from django.contrib.auth.views import LoginView  # not delete
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



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
    success_url = reverse_lazy("success_registration")

    def form_valid(self, form):
        try:
            if form.data["subscribe_check"]:
                create_new_subscribe(email=form.data["email"], auth=True)
        except:
            pass
        create_user(form.data["email"], form.data["password"])
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data())


def success_registration(request):
    return render(request, "profile/success_registration.html")


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            valid_form = form.cleaned_data
            user = authenticate(request,
                                username=create_username_from_email(valid_form["email"]),
                                password=valid_form["password"])
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.info(request, "Something going wrong !!!")
    else:
        form = LoginForm()
    return render(request, "profile/sign_in.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect("home")

""" # not delete, need remake registration form, for register with username
class LoginUser(LoginView):
    template_name = "profile/sign_in.html"
    form_class = LoginForm
    redirect_field_name = "home"
"""