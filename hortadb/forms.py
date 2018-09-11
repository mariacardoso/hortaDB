from django import forms

from .models import Species

class SpeciesForm(forms.Form):

    species = forms.CharField(
        help_text = 'Enter the species.',
        max_length = 100,
    )