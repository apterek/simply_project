from profiles.models import ProfileInformation
from django.db.models import QuerySet


def user_information(user_id: int) -> QuerySet:
    return ProfileInformation.objects.all().filter(user_id=user_id).first()


def update_user_information(name, bday, gender, about, status, profile_photo) -> None:
    pass
