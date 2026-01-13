from django import forms
from .models import Link
from django.core.exceptions import ValidationError


class NewLinkForm(forms.ModelForm):

    class Meta:
        model = Link
        fields = ['name', 'link_url', 'description']
