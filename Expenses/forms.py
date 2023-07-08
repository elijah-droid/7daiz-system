from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = ['Reason', 'Amount']
        widgets = {
            'Reason': forms.TextInput(attrs={'class': 'form-control'}),
            'Amount': forms.NumberInput(attrs={'class': 'form-control'})
        }
