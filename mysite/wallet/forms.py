from django import forms
from .models import Income, PurchasedGoods
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class UserRegisterForm(UserCreationForm):
    """Form for filling in information about user to registrate"""
    captcha = CaptchaField()

    def clean_username(self):
        """Validate field value. First character must be a letter"""
        username = self.cleaned_data['username']
        if re.match(r'\d', username):
            raise ValidationError('First character must be a letter')
        return username

    def __init__(self, *args, **kwargs):
        """Set attributes for fields"""
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password from numbers and letters'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Repeat password'})
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {
            'username': None,
            'email': None,
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username',
                                               'autocomplete': 'off'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail address',
                                             'autocomplete': 'off'}),
        }


class UserLoginForm(AuthenticationForm):
    """Form for filling in information about user to login"""

    def clean_username(self):
        """Validate field value. First character must be a letter"""
        username = self.cleaned_data['username']
        if re.match(r'\d', username):
            raise ValidationError('First character must be a letter')
        return username

    def __init__(self, *args, **kwargs):
        """Set attributes for fields"""
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username', 'autocomplete': 'off'})
        self.fields['password'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password from numbers and letters', 'autocomplete': 'off'})
        self.fields['username'].help_text = ''
        self.fields['password'].help_text = ''


class ChangePasswordForm(PasswordChangeForm):
    """Form for filling in information to change password"""

    def __init__(self, *args, **kwargs):
        """Set attributes for fields"""
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Old password'})
        self.fields['new_password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'New password'})
        self.fields['new_password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Repeat password'})
        self.fields['old_password'].help_text = ''
        self.fields['new_password1'].help_text = ''
        self.fields['new_password2'].help_text = ''

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
        help_texts = {
            'old_password': None,
            'new_password1': None,
            'new_password2': None,
        }
        widgets = {
            'old_password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'old_password',
                                                       'autocomplete': 'off'}),
            'new_password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'new_password1',
                                                        'autocomplete': 'off'}),
            'new_password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'new_password2',
                                                        'autocomplete': 'off'}),
        }


class IncomeForm(forms.ModelForm):
    """Form for filling in information about incomes"""

    def __init__(self, *args, **kwargs):
        """Set attributes for field"""
        super(IncomeForm, self).__init__(*args, **kwargs)
        self.fields['amount_of_income'].widget.attrs['min'] = 0.01

    def clean_type_of_income(self):
        """Validate field value. Field must contain only letters"""
        type_of_income = self.cleaned_data['type_of_income']
        if re.findall(r'\d', type_of_income):
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
        """Set attributes for fields"""
        super(PurchaseForm, self).__init__(*args, **kwargs)
        self.fields['price_per_item'].widget.attrs['min'] = 0.01
        self.fields['quantity_of_goods'].widget.attrs['min'] = 1
        self.fields['category'].empty_label = 'Please select category'

    def clean_name_of_product(self):
        """Validate field value. Field must contain only letters"""
        name_of_product = self.cleaned_data['name_of_product']
        if re.findall(r'\d', name_of_product):
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
