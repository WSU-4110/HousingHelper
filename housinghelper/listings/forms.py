from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Listing
from django import forms
from django.contrib.auth.models import User
import calculation

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ('title', 'description', 'price', 'bedrooms', 'bathrooms', 'garage', 'sqft', 'lot_size','image','choice')


class CreateUserForm(UserCreationForm):
    class meta:
        model = User
        fields = ('username', 'password1', 'password2')



class TestForm(forms.Form):
    down_payment = forms.DecimalField()
    price = forms.DecimalField()
    interest_rate = forms.DecimalField()
    term = forms.IntegerField()
    amount = forms.DecimalField(
        widget=calculation.FormulaInput('(down_payment*price)/(term*interest_rate)') # <- using single math expression
    )
