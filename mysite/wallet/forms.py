from django import forms
from .models import Income, PurchasedGoods
import re
from django.core.exceptions import ValidationError


class IncomeForm(forms.ModelForm):
    """Form for filling in information about incomes"""

    def __init__(self, *args, **kwargs):
        """Set attributes for field"""
        super(IncomeForm, self).__init__(*args, **kwargs)
        self.fields['amount_of_income'].widget.attrs['min'] = 0.01

    def clean_type_of_income(self):
        """Validate field value. Field must contain only letters"""
        type_of_income = self.cleaned_data['type_of_income']
        if re.match(r'\d', type_of_income):
            raise ValidationError('You can use only letters in field "Type of income"')
        return type_of_income

    class Meta:
        model = Income
        fields = ['type_of_income', 'amount_of_income']
        widgets = {
            'type_of_income': forms.TextInput(attrs={"class": "form-control"}),
            'amount_of_income': forms.NumberInput(attrs={"class": "form-control"})
        }


class PurchaseForm(forms.ModelForm):
    """Form for filling in information about purchased goods"""

    def __init__(self, *args, **kwargs):
        """Set attributes for field"""
        super(PurchaseForm, self).__init__(*args, **kwargs)
        self.fields['price_per_item'].widget.attrs['min'] = 0.01
        self.fields['quantity_of_goods'].widget.attrs['min'] = 1
        self.fields['category'].empty_label = 'Please select category'

    def clean_name_of_product(self):
        """Validate field value. Field must contain only letters"""
        name_of_product = self.cleaned_data['name_of_product']
        if re.match(r'\d', name_of_product):
            raise ValidationError('You can use only letters in field "Name of product"')
        return name_of_product

    class Meta:
        model = PurchasedGoods
        fields = ['name_of_product', 'price_per_item', 'quantity_of_goods', 'category']
        widgets = {
            'name_of_product': forms.TextInput(attrs={'class': 'form-control'}),
            'price_per_item': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity_of_goods': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }
