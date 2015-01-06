from django.forms import forms, ModelChoiceField
from submit.models import Assignment


class UploadFileForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='Max size: 1 megabytes'
    )

    assignments = ModelChoiceField(queryset=Assignment.objects.all())
    #TOOD VALIDATE