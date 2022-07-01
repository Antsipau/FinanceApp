from datetime import date

from django.db.models import Sum
from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal

from .models import Income


def main_page(request):
    return HttpResponse("It will be home page")


def income(request):
    my_income = Income.objects.all()
    res = '<h1>My incomes</h1>'
    for i in my_income:
        res += f'<div>\n<p>{i.date_of_income}</p>\n<p>You received {i.amount_of_income}</p>\n</div>\n<hr>\n'
    return HttpResponse(res)


def my_total_income(request):
    total = Income.objects.aggregate(TOTAL=Sum('amount_of_income'))['TOTAL']
    res = '<h1> My total income:</h1>' f'<div>\n<p>Today is {date.today()}</p>\n<p>Your total income:{total}</p>\n</div>'
    return HttpResponse(res)


def test(request):
    return HttpResponse("<h1>Test page</h1>")
