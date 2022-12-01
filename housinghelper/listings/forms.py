from django.forms import ModelForm
from .models import Listing
from django import forms
import calculation

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ('title', 'description', 'price', 'bedrooms', 'bathrooms', 'garage', 'sqft', 'lot_size','image','choice')


class TestForm(forms.Form):
    down_payment = forms.DecimalField()
    price = forms.DecimalField()
    interest_rate = forms.DecimalField()
    term = forms.IntegerField()
    amount = forms.DecimalField(
        widget=calculation.FormulaInput('(down_payment*price)/(term*interest_rate)') # <- using single math expression
     #widget=calculation.FormulaInput('(0.28*price*term)+(down_payment)')
        )
