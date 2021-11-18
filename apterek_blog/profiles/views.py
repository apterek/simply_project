from django.views.generic import TemplateView, CreateView, UpdateView
from profiles.forms import EditProfileInfoForm
from profiles.models import ProfileInformation
from core.models import Post
from profiles.services import user_information, update_user_information


class ProfileView(TemplateView):
    template_name = "profile/user_profile_page.html"

    def get_context_data(self, **kwargs):

        if self.request.user.is_authenticated:
            profile = user_information(self.request.user.id)
            posts = Post.objects.all().filter(author_id=self.request.user.id)
            return {"profile": profile, "posts": posts}


class UpdateProfile(CreateView):
    template_name = "profile/update_profile_page.html"

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            profile = user_information(self.request.user.id)
            form = EditProfileInfoForm()
            return {"profile": profile, "form": form}

    def post(self, request, *args, **kwargs):
        update_form = EditProfileInfoForm(self.request.POST)
        if update_form.is_valid():
            update_user_information(**update_form.cleaned_data)

