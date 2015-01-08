from django.contrib.auth.forms import AuthenticationForm
from django.forms import forms, ModelChoiceField, CharField
from django.forms.widgets import *
from submit.models import Assignment


class UploadFileForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='Max size: 1 megabytes'
    )

    assignments = ModelChoiceField(queryset=Assignment.objects.all())
    #TOOD VALIDATE


class LoginForm(AuthenticationForm):
    username = CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
    password = CharField(widget=PasswordInput(attrs={'placeholder': 'Password'}))