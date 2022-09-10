
from django import forms

from .models import *
 
class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ["symbol"]
        labels = {
            'symbol': 'Symbol',
        }
        widgets = {
            'symbol': forms.Select(attrs={'class':"choice","required":"false"})
        }