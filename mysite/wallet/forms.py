from django import forms
from .models import Category


class IncomeForm(forms.Form):
    """Form for filling in information about incomes"""
    type_of_income = forms.CharField(max_length=255, required=True,
                                     widget=forms.TextInput(attrs={"class": "form-control"}))
    amount_of_income = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.1,
                                          widget=forms.NumberInput(attrs={"class": "form-control"}))


class PurchaseForm(forms.Form):
    """Form for filling in information about purchased goods"""
    name_of_product = forms.CharField(max_length=255, required=True,
                                      widget=forms.TextInput(attrs={"class": "form-control"}))
    price_per_item = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.1,
                                        widget=forms.NumberInput(attrs={"class": "form-control"}))
    quantity_of_goods = forms.IntegerField(min_value=1)
    category = forms.ModelChoiceField(empty_label='Select a category', queryset=Category.objects.all())
