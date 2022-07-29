from django import forms


class IncomeForm(forms.Form):
    """Form that consists of 2 fields: Type of income, Amount of income User must fill in these fields"""
    type_of_income = forms.CharField(max_length=255, required=False,
                                     widget=forms.TextInput(attrs={"class": "form-control"}))
    amount_of_income = forms.DecimalField(max_digits=10, decimal_places=2,
                                          widget=forms.NumberInput(attrs={"class": "form-control"}))
