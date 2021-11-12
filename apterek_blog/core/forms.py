from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm


class SubscriberForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control",
               "placeholder": "Email"}),
        required=False)


class RegistrationForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control"}))
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(
        attrs={"class": "form-control"}), max_length=30)
    confirm_password = forms.CharField(min_length=8, widget=forms.PasswordInput(
        attrs={"class": "form-control"}), max_length=30)
    subscribe_check = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={"class": "form-check-input"}), required=False)

    def clean_email(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email already is used")
        return cleaned_data

    def clean_confirm_password(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password:
            if password != confirm_password:
                raise ValidationError("Password will be math !!!")
        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(
        attrs={"class": "form-control"}), max_length=30)
