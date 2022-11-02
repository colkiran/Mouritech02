
from django import forms
from .models import Product
from django.core import validators

class ProductDetails(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Prodid', 'Prodname', 'Category', 'Prodtype', 'Price']
        widgets = {
            'Prodid': forms.TextInput(attrs={'class': 'form-control'}),
            'Prodname': forms.TextInput(attrs={'class': 'form-control'}),
            'Category': forms.TextInput(attrs={'class': 'form-control'}),
            'Prodtype': forms.TextInput(attrs={'class': 'form-control'}),
            'Price': forms.TextInput(attrs={'class': 'form-control'}),
        }