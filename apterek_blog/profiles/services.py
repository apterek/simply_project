from profiles.models import ProfileInformation
from django.db.models import QuerySet
import os


def user_information(user_id: int) -> QuerySet:
    return ProfileInformation.objects.all().filter(user_id=user_id).first()


def update_user_information(update_form, user_id: int) -> None:
    if update_form.cleaned_data["name"]:
        ProfileInformation.objects.all().filter(user_id=user_id).\
            update(name=update_form.cleaned_data["name"])
    if update_form.cleaned_data["bday"]:
        ProfileInformation.objects.all().filter(user_id=user_id).\
            update(bday=update_form.cleaned_data["bday"])
    if update_form.cleaned_data["gender"]:
        ProfileInformation.objects.all().filter(user_id=user_id).\
            update(gender=update_form.cleaned_data["gender"])
    if update_form.cleaned_data["about"]:
        ProfileInformation.objects.all().filter(user_id=user_id).\
            update(about=update_form.cleaned_data["about"])
    if update_form.cleaned_data["status"]:
        ProfileInformation.objects.all().filter(user_id=user_id).\
            update(status=update_form.cleaned_data["status"])
    if update_form.cleaned_data["profile_photo"]:
        new_image = ProfileInformation.objects.filter(user_id=user_id).first()
        ProfileInformation.objects.filter(user_id=user_id).first().profile_photo.delete()
        new_image.profile_photo = update_form.cleaned_data["profile_photo"]
        new_image.save()


