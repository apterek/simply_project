from django import forms


class SubscriberForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control",
               "placeholder": "Email"}),
        required=False)


class RegistrationForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(
        attrs={"class": "form-control"}), max_length=30)
    confirm_password = forms.CharField(min_length=8, widget=forms.PasswordInput(
        attrs={"class": "form-control"}), max_length=30)


class SignInForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(
        attrs={"class": "form-control"}), max_length=30)
