from django import forms
from .models import Printing


class PrintingForm(forms.ModelForm):

    class Meta:
        model = Printing
        fields = ['Paper', 'No_of_Papers', 'Amount_Paid']
        widgets = {
            'Paper': forms.Select(attrs={'class': 'form-control'}),
            'No_of_Papers': forms.NumberInput(attrs={'class': 'form-control'}),
            'Amount_Paid': forms.NumberInput(attrs={'class': 'form-control'})
        }