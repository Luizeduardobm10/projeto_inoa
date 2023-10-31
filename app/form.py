from django import forms

from .models import React

class AtivoForm(forms.ModelForm):
    class Meta:
        model = React
        fields =['symbol','name']