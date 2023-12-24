from django import forms
from .models import Sale


class SalesForm(forms.ModelForm):

    class Meta:
        model = Sale
        fields = ['Product', 'Quantity', 'Money_Collected', 'Staff']
        widgets = {
            'Product': forms.Select(attrs={'class': 'form-control'}),
            'Quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'Money_Collected': forms.NumberInput(attrs={'class': 'form-control'}),
            'Staff': forms.Select(attrs={'class': 'form-control'})
        }