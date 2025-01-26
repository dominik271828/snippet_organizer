from django import forms
from .models import Snippet
from django.db import models
from datetime import datetime


class SnippetUpdateForm(forms.ModelForm):
    title = models.CharField(max_length=100)
    data = models.CharField(max_length=100)

    class Meta:
        model = Snippet
        fields = ['title', 'data', 'lang', 'pub_date', 'owner']
        widgets = {
            'data': forms.Textarea(),
            'pub_date': forms.DateInput(attrs={'value':datetime.now}), 
            'owner': forms.HiddenInput(),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['owner'].required = False