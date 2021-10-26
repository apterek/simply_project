from django.shortcuts import redirect
from core.models import Post
from core.services import take_a_three_best_post, create_new_subscribe, search_post
from core.forms import SubscriberForm
from django.views.generic import CreateView
from django.contrib import messages


class HomepageView(CreateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        search_query = self.request.GET.get("search_field", None)
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

