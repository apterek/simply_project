from django import forms


# form for uploading multiple files
class FileForm(forms.Form):
    filename = forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple": True}), required=False)
