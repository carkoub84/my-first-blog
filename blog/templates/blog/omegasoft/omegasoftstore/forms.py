# File: Omegasoft/forms.py
# Purpose: Define forms for the Omegasoft app

from django import forms

class AddToCartForm(forms,forms.Form):
    quantity = forms.IntegerField()