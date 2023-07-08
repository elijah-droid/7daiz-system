from django import forms 
from .models import Stock


class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ['Product', 'Quantity', 'Price', 'Alert_Level']
        widgets = {
            'Product': forms.Select(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'Quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'Price': forms.NumberInput(attrs={'class': 'form-control'}),
            'Alert_Level': forms.NumberInput(attrs={'class': 'form-control'}),
        }