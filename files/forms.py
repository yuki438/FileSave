from django import forms
from .models import File

class UploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['uploaded_file', 'name']

class FilterForm(forms.Form):
    filter = forms.ChoiceField(initial='date', choices=[
        ('date', 'by date'),
        ('name', 'by name'),
    ])