from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView
from profiles.forms import EditProfileInfoForm
from core.models import Post
from profiles.services import user_information, update_user_information


# viewing the profile of the current user
class ProfileView(TemplateView):
    template_name = "profile/user_profile_page.html"

    def get_context_data(self, **kwargs):

        if self.request.user.is_authenticated:
            profile = user_information(self.request.user.id)
            posts = Post.objects.all().filter(author_id=self.request.user.id)
            return {"profile": profile, "posts": posts}


# update the profile of the current user
class UpdateProfile(CreateView):
    template_name = "profile/update_profile_page.html"

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            profile = user_information(self.request.user.id)
            form = EditProfileInfoForm()
            return {"profile": profile, "form": form}

    def post(self, request, *args, **kwargs):
        update_form = EditProfileInfoForm(request.POST, request.FILES)
        if update_form.is_valid():
            update_user_information(update_form, self.request.user.id)
            return redirect("profile_url")


