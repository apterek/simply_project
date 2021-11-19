import datetime
from django import forms
from profiles.models import ProfileInformation, GENDER_SETTING

DATE_INPUT_FORMAT = ['%d-%m-%Y']


class EditProfileInfoForm(forms.Form):
    name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(
        attrs={"placeholder": "Update your name", "class": "form-control"}))
    bday = forms.DateField(widget=forms.SelectDateWidget(), initial=datetime.date.today)
    gender = forms.ChoiceField(choices=GENDER_SETTING,
                               widget=forms.Select(attrs={"class": "form-select"}), required=False)
    about = forms.CharField(max_length=2000, required=False, widget=forms.Textarea(
        attrs={"class": "form-control", "placeholder": "Update information about you"}))
    status = forms.CharField(max_length=30, required=False, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Update your status"}))
    profile_photo = forms.ImageField(required=False)
