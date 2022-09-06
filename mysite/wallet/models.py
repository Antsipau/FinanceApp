from django.db import models
from django.urls import reverse
from django.db.models import Sum


class Income(models.Model):
    """This model describes incomes"""
    date_of_income = models.DateField(auto_now_add=True, db_index=True, verbose_name='Date')
    type_of_income = models.CharField(max_length=255, null=True, blank=True, verbose_name='Type of income')
    amount_of_income = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                           verbose_name='Amount of income')

    @staticmethod
    def my_total_income():
        """Sum the values оf the column: 'amount_of_income' """
        total = Income.objects.aggregate(TOTAL=Sum('amount_of_income'))['TOTAL']
        result = f'Your total income is: {total:.2f}'
        return result

    def __str__(self):
        return self.type_of_income

    class Meta:
        verbose_name = 'Income'
        verbose_name_plural = 'Incomes'
        ordering = ['-date_of_income']


class PurchasedGoods(models.Model):
    """This model describes list of purchased goods"""
    date_of_purchase = models.DateField(auto_now_add=True, db_index=True, verbose_name='Date')
    name_of_product = models.CharField(max_length=255, null=True, blank=True, verbose_name='Name of product')
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                         verbose_name='Price per item')
    quantity_of_goods = models.IntegerField(null=True, blank=True, verbose_name='Quantity of goods')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Category')

    def __str__(self):
        return self.name_of_product

    class Meta:
        verbose_name = 'Purchased good'
        verbose_name_plural = 'Purchased goods'
        ordering = ['-date_of_purchase']


class Category(models.Model):
    """This model contains categories of expenses"""
    title = models.CharField(max_length=255, db_index=True, verbose_name='Name of category')

    def get_absolute_url(self):
        """Get a certain category"""
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']
