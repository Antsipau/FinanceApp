from datetime import date
from django.db import models


class Income(models.Model):
    """This model describes incomes"""
    date_of_income = models.DateField(auto_now_add=True)
    amount_of_income = models.DecimalField(..., max_digits=10, decimal_places=2)


class PurchasedGoods(models.Model):
    """This model describes list of purchased goods"""
    date_of_purchase = models.DateField(auto_now_add=True)
    nameof_product = models.CharField(max_length=255)
    price_per_item = models.DecimalField(..., max_digits=10, decimal_places=2)
    quantity_of_goods = models.IntegerField()

