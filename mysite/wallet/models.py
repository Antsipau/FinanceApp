from django.db import models


class Income(models.Model):
    """This model describes incomes"""
    date_of_income = models.DateField(auto_now_add=True, db_index=True, verbose_name='Date')
    amount_of_income = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name='Amount of income')


class TotalIncome(models.Model):
    """This model consists of summery of my incomes"""
    total_income = models.DecimalField(max_digits=20, decimal_places=2, null=True, verbose_name='Total income')
    total_income_date = models.DateField(auto_now=True, db_index=True, verbose_name='Date')


class PurchasedGoods(models.Model):
    """This model describes list of purchased goods"""
    date_of_purchase = models.DateField(auto_now_add=True, db_index=True, verbose_name='Date')
    name_of_product = models.CharField(max_length=255, null=True, verbose_name='Name of product')
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name='Price per item')
    quantity_of_goods = models.IntegerField(null=True, verbose_name='Quantity of goods')
    amount_of_expenses = models.DecimalField(max_digits=20, decimal_places=2, null=True,
                                             verbose_name='Amount of expenses')


class TotalExpenses(models.Model):
    """This model consists of summery of expenses"""
    total_expenses = models.DecimalField(max_digits=20, decimal_places=2, null=True, verbose_name='Total expenses')
    total_expanses_date = models.DateField(auto_now=True, db_index=True, verbose_name='Date')


class WalletBalance(models.Model):
    """This model has information about wallet balance"""
    wallet_balance = models.DecimalField(max_digits=20, decimal_places=2, null=True, verbose_name='Amount of expenses')
    date_of_balance = models.DateField(auto_now_add=True, db_index=True, verbose_name='Date')
