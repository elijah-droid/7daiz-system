from django import forms
from .models import Report


class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = ['Sales', 'Printing', 'Grand_Total', 'Balance', 'Cash_Taken']
        widgets = {
            'Sales': forms.NumberInput(attrs={'class': 'form-control', 'readonly': ''}),
            'Printing': forms.NumberInput(attrs={'class': 'form-control', 'readonly': ''}),
            'Grand_Total': forms.NumberInput(attrs={'class': 'form-control', 'readonly': ''}),
            'Balance': forms.NumberInput(attrs={'class': 'form-control', 'readonly': ''}),
            'Cash_Taken': forms.NumberInput(attrs={'class': 'form-control'}),
        }