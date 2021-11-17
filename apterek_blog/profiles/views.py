from django.views.generic import TemplateView, UpdateView
from profiles.forms import EditProfileInfoForm
from profiles.models import ProfileInformation
from core.models import Post


class ProfileView(TemplateView):
    template_name = "profile/user_profile_page.html"

    def get_context_data(self, **kwargs):

        if self.request.user.is_authenticated:
            profile = ProfileInformation.objects.all().filter(user_id=self.request.user.id).first()
            posts = Post.objects.all().filter(author_id=self.request.user.id)
            return {"profile": profile, "posts": posts}


class UpdateProfile(UpdateView):
    template_name = "profile/update_profile_page.html"
    form_class = EditProfileInfoForm
    success_url = "profile_url"



