import datetime
from django import forms
from profiles.models import ProfileInformation, GENDER_SETTING


DATE_INPUT_FORMAT = ['%d-%m-%Y']


class EditProfileInfoForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"placeholder": "Update your name"}))
    bday = forms.DateField(widget=forms.SelectDateWidget(), initial=datetime.date.today)
    gender = forms.ChoiceField(choices=GENDER_SETTING,
                               widget=forms.Select(attrs={"class": "ml-1 mr-3"}), required=False)
    about = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={"class": "form-control",
                                                                          "rows": 6,
                                                                          "placeholder": "Update information about you"}))
    status = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"class": "form-control",
                                                                          "placeholder": "Update your status"}))
    profile_photo = forms.ImageField()
