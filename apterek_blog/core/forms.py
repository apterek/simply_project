from django import forms


class SubscriberForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control",
               "placeholder": "Email"}),
        required=False)
