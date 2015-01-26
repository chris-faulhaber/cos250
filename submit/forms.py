from django.contrib.auth.forms import AuthenticationForm
from django.forms import forms, ModelChoiceField, CharField
from django.forms.widgets import *
from submit.models import Part
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UploadFileForm(forms.Form):

    docfile = forms.FileField(label='Select a file', help_text='Max size: 1 megabytes')
    #TOOD VALIDATE
    part = ModelChoiceField(queryset=Part.objects.all())

    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit'
        self.helper.add_input(Submit('submit', 'Submit'))

    def is_valid(self):
        try:
            docfile = self.files['docfile']
        except KeyError:
            return False & super(UploadFileForm, self).is_valid()

        if docfile.size > 10000:
            raise forms.ValidationError('File too large.')

        return self.is_bound and not bool(self.errors)


class LoginForm(AuthenticationForm):
    username = CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
    password = CharField(widget=PasswordInput(attrs={'placeholder': 'Password'}))
