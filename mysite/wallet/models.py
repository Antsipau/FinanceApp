from datetime import datetime, timedelta
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Income(models.Model):
    """This model describes incomes"""
    date_of_income = models.DateField(auto_now_add=True, db_index=True, verbose_name='Date')
    type_of_income = models.CharField(max_length=255, null=True, verbose_name='Type of income')
    amount_of_income = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                           verbose_name='Amount of income')
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, verbose_name='User')

    @staticmethod
    def total_user_income(request):
        """Sum the values of the column: 'amount_of_income' for a specific user"""
        total_income_result = 0
        for i in request.user.income_set.all():
            total_income_result += i.amount_of_income
        return f'Your total income for the entire period: {total_income_result:.2f}.'

    @staticmethod
    def previous_year_income(request):
        """Sum income for previous year"""
        previous_year = datetime.today().year - 1
        total_income_result = 0
        result = request.user.income_set.all()
        for i in result.filter(date_of_income__year=previous_year):
            total_income_result += i.amount_of_income
        return f'Your income in  previous {previous_year} year: ' \
               f'{total_income_result:.2f}.'

    @staticmethod
    def current_year_income(request):
        """Sum income for current year"""
        current_year = datetime.now().year
        total_income_result = 0
        result = request.user.income_set.all()
        for i in result.filter(date_of_income__year=current_year):
            total_income_result += i.amount_of_income
        return f'Your income in current {current_year} year: ' \
               f'{total_income_result:.2f}.'

    @staticmethod
    def income_difference(request):
        """Calculate income difference"""
        current_year = datetime.now().year
        previous_year = datetime.today().year - 1
        current_year_income = 0
        previous_year_income = 0
        result = request.user.income_set.all()
        for i in result.filter(date_of_income__year=current_year):
            current_year_income += i.amount_of_income
        for i in result.filter(date_of_income__year=previous_year):
            previous_year_income += i.amount_of_income
        total_income_difference = current_year_income - previous_year_income
        if current_year_income < previous_year_income:
            return f"In {current_year} year, you earned {-total_income_difference} less than last {previous_year} year."
        if current_year_income > previous_year_income:
            return f"In {current_year} year, you earned {total_income_difference} more than last {previous_year} year."
        if current_year_income == previous_year_income:
            return f"You earned the same amount this {current_year} year as you did last {previous_year} year."

    @staticmethod
    def previous_month_income(request):
        """Sum income for previous month of current year"""
        current_year = datetime.now().year
        previous_month = datetime.now().month - 1
        total_income_result = 0
        result = request.user.income_set.all()
        for i in result.filter(date_of_income__year=current_year, date_of_income__month=previous_month):
            total_income_result += i.amount_of_income
        return f'Your income in {previous_month} {datetime.now().strftime("%Y")} year: ' \
               f'{total_income_result:.2f}.'

    @staticmethod
    def current_month_income(request):
        """Sum income for current month of current year"""
        current_year = datetime.now().year
        current_month = datetime.now().month
        total_income_result = 0
        result = request.user.income_set.all()
        for i in result.filter(date_of_income__year=current_year, date_of_income__month=current_month):
            total_income_result += i.amount_of_income
        return f'Your income in {datetime.now().strftime("%B")} {datetime.now().strftime("%Y")} year: ' \
               f'{total_income_result:.2f}.'

    def __str__(self):
        return self.type_of_income

    class Meta:
        verbose_name = 'Income'
        verbose_name_plural = 'Incomes'
        ordering = ['-id']


class PurchasedGoods(models.Model):
    """This model describes list of purchased goods"""
    date_of_purchase = models.DateField(auto_now_add=True, db_index=True, verbose_name='Date')
    name_of_product = models.CharField(max_length=255, null=True, verbose_name='Name of product')
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                         verbose_name='Price per item')
    quantity_of_goods = models.IntegerField(null=True, blank=True, verbose_name='Quantity of goods')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Category')
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, verbose_name='User')

    @staticmethod
    def user_expenses(request):
        """Sum the values of the columns 'price_per_item' multiplied 'quantity_of_goods' for a specific user"""
        total_expenses_result = 0
        for i in request.user.purchasedgoods_set.all():
            total_expenses_result += i.price_per_item * i.quantity_of_goods
        return f'Your total expenses: {total_expenses_result:.2f}'

    # @staticmethod
    # def (request):
    #     """Sum the values of the column: 'price_per_item' for a specific user"""
    #     total_expenses_result = 0
    #     for i in request.user.purchasedgoods_set.all():
    #         total_expenses_result += i.price_per_item * i.quantity_of_goods
    #     return f'Your total expenses: {total_expenses_result:.2f}'

    def __str__(self):
        return self.name_of_product

    class Meta:
        verbose_name = 'Purchased good'
        verbose_name_plural = 'Purchased goods'
        ordering = ['-id']


class Category(models.Model):
    """This model contains categories of expenses"""
    title = models.CharField(max_length=255, db_index=True, verbose_name='Name of category')

    def get_absolute_url(self):
        """Get a certain category"""
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']
