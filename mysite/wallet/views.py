from datetime import date

from django.db.models import Sum
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import IncomeForm, PurchaseForm
from .models import Income, PurchasedGoods, Category


def main_page(request):
    """Function to display home page"""
    return render(request, 'wallet/main_page.html', {'title': 'Home page'})


def income(request):
    """function to display income page"""
    my_income = Income.objects.all()
    return render(request, 'wallet/income_page.html', {'my_income': my_income, 'title': 'My incomes'})


def my_total_income(request):
    total = Income.objects.aggregate(TOTAL=Sum('amount_of_income'))['TOTAL']
    res = '<h1> My total income:</h1>' \
          f'<div>\n' \
          f'<p>Today is {date.today()}</p>\n' \
          f'<p>Your total income:{total:.2f}</p>\n' \
          f'</div>'
    return HttpResponse(res)


def my_purchased_goods(request):
    """Function to display purchased goods"""
    my_goods = PurchasedGoods.objects.all()
    categories = Category.objects.all()
    context = {
        'my_goods': my_goods,
        'title': 'Purchased goods',
        'categories': categories
    }

    return render(request, 'wallet/purchased_goods_page.html', context=context)


def add_income(request):
    """Function to add information into Income Model (database)"""
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            Income.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = IncomeForm()
    return render(request, 'wallet/add_income_page.html', {'form': form, 'title': 'Add income'})


def add_purchase(request):
    """Function to add information into PurchasedGoods Model (database)"""
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            PurchasedGoods.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = PurchaseForm()
    return render(request, 'wallet/add_purchase_page.html', {'form': form, 'title': 'Add purchase'})


def get_category(request, category_id):
    """Function to get category of purchased goods"""
    goods = PurchasedGoods.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'wallet/category.html', {'goods': goods, 'categories': categories, 'category': category,
                                                    'title': 'Purchased goods'})


