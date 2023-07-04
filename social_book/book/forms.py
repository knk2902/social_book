from django import forms
from .models import UploadedBook

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedBook
        fields = ['title', 'file', 'description', 'visibility', 'cost', 'year_published']
