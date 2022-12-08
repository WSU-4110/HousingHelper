from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Listing
from django import forms
from django.contrib.auth.models import User
import calculation

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ('title', 'description', 'price', 'bedrooms', 'bathrooms', 'garage', 'sqft', 'lot_size','image','choice','housing_type')
        exclude = ['favorites']


class CreateUserForm(UserCreationForm):
    class meta:
        model = User
        fields = ('username', 'password1', 'password2')


# widget=calculation.FormulaInput('loan_total*(((interest_rate)*(1+interest_rate)^loan_term)/(1+interest_rate)^(loan_term - 1))') # <- using single math expression
class TestForm(forms.Form):
    loan_total = forms.IntegerField()
    interest_rate = forms.FloatField()
    loan_term = forms.IntegerField()
    
    amount = forms.DecimalField(
        

            widget= calculation.FormulaInput(
                'loan_total*(((interest_rate/12)*(1+(interest_rate/12))**loan_term)/((1+(interest_rate/12))**loan_term-1))'
                
                ) # <- using single math expression
     #widget=calculation.FormulaInput('(0.28*price*term)+(down_payment)')


    )
    
    
    Total_cost_over_term = forms.DecimalField( widget= calculation.FormulaInput(
               'amount*120'               
                ))
