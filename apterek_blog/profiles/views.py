from django.shortcuts import redirect
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
        update_form = EditProfileInfoForm(request.POST, request.FILES)

        if update_form.is_valid():
            print(update_form.cleaned_data["profile_photo"])
            update_user_information(update_form, self.request.user.id)
            #ProfileInformation.objects.all().filter(user_id=self.request.user.id).update(**update_form.cleaned_data)
            #ProfileInformation.objects.update_or_create(**update_form.cleaned_data)
            #update_user_information(**update_form.cleaned_data)
            return redirect("profile_url")


