from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['Name', 'Type', 'Price']
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Type': forms.Select(attrs={'class': 'form-control'}),
            'Price': forms.NumberInput(attrs={'class': 'form-control'})
        }