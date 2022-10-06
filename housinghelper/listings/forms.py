from django.forms import ModelForm
from .models import Listing
from django import forms
import calculation

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ('title', 'description', 'price', 'bedrooms', 'bathrooms', 'garage', 'sqft', 'lot_size')


class TestForm(forms.Form):
    quantity = forms.DecimalField()
    price = forms.DecimalField()
    amount = forms.DecimalField(
        widget=calculation.FormulaInput('quantity*price') # <- using single math expression
    )
    apply_taxes = forms.BooleanField(initial=True)
    tax = forms.DecimalField(
        # using math expression and javascript functions.
        widget=calculation.FormulaInput('apply_taxes ? parseFloat(amount/11).toFixed(2) : 0.0') 
    )
