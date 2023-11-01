from django import forms

from .models import React

class AtivoList(forms.ModelForm):
    class Meta:
        model = React
        fields =['symbol','name']