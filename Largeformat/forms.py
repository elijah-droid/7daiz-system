from django import forms
from .models import LargeformatPrinting, Roll


class LargeFormatForm(forms.ModelForm):

    class Meta:
        model = LargeformatPrinting
        fields = ['Roll', 'Width_Printed', 'Height_Printed', 'Amount_Paid', 'Staff']
        widgets = {
            'Roll': forms.Select(attrs={'class': 'form-control'}),
            'Width_Printed': forms.NumberInput(attrs={'class': 'form-control'}),
            'Height_Printed': forms.NumberInput(attrs={'class': 'form-control'}),
            'Amount_Paid': forms.NumberInput(attrs={'class': 'form-control'}),
            'Staff': forms.Select(attrs={'class': 'form-control'}),

        }


class RollForm(forms.ModelForm):
    class Meta:
        model = Roll
        fields = ['Type', 'Width', 'Price_per_sq_meter', 'Rolls_Available', 'Meters_Left']
        widgets = {
            'Type': forms.Select(attrs={'class': 'form-control'}),
            'Width': forms.NumberInput(attrs={'class': 'form-control'}),
            'Price_per_sq_meter': forms.NumberInput(attrs={'class': 'form-control'}),
            'Rolls_Available': forms.NumberInput(attrs={'class': 'form-control'}),
            'Meters_Left': forms.NumberInput(attrs={'class': 'form-control'}),
        }