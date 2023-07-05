from django import forms
from .models import Report


class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = ['Sales', 'Printing', 'Grand_Total', 'Cash_Taken']
        widgets = {
            'Sales': forms.NumberInput(attrs={'class': 'form-control'}),
            'Printing': forms.NumberInput(attrs={'class': 'form-control'}),
            'Grand_Total': forms.NumberInput(attrs={'class': 'form-control'}),
            'Cash_Taken': forms.NumberInput(attrs={'class': 'form-control'}),
        }