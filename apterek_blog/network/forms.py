from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from network.models import TopologyImages


class FileForm(forms.Form):
    filename = forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple": True}), required=False)
