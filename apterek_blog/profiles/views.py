from django.views.generic import TemplateView
from profiles.forms import EditProfileInfoForm
from profiles.models import ProfileInformation


class ProfileView(TemplateView):
    template_name = "profile/user_profile_page.html"

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            profile = ProfileInformation.objects.filter(user_id=self.request.user.id)
            return {"profile": profile}
