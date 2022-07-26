from datetime import date

from django.db.models import Sum
from django.shortcuts import render
from django.http import HttpResponse

from .models import Income, PurchasedGoods


def main_page(request):
    my_income = Income.objects.all()
    return render(request, 'wallet/main_page.html', {'my_income': my_income, 'title': 'Home page'})


def income(request):
    my_income = Income.objects.all()
    return render(request, 'wallet/income.html', {'my_income': my_income, 'title': 'My incomes'})


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


def test(request):
    return HttpResponse("<h1>Test page</h1>")
