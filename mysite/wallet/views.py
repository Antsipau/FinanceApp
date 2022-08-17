from datetime import date

from django.db.models import Sum
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import IncomeForm, PurchaseForm
from .models import Income, PurchasedGoods


def main_page(request):
    my_income = Income.objects.all()
    return render(request, 'wallet/main_page.html', {'my_income': my_income, 'title': 'Home page'})


def income(request):
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
    my_goods = PurchasedGoods.objects.all()
    return render(request, 'wallet/purchased_goods_page.html', {'my_goods': my_goods, 'title': 'Purchased goods'})


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
