from django import forms
from .models import Paper


class PaperForm(forms.ModelForm):

    class Meta:
        model = Paper
        fields = ['product', 'format', 'Size', 'Price']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'format': forms.Select(attrs={'class': 'form-control'}),
            'Size': forms.Select(attrs={'class': 'form-control'}),
            'Price': forms.NumberInput(attrs={'class': 'form-control'})
        }