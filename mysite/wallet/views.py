from django.shortcuts import render
from django.http import HttpResponse

from .models import Income

def main_page(request):
    return HttpResponse("It will be home page")

def income(request):
    my_income = Income.objects.all()
    res = '<h1>My incomes</h1>'
    for i in my_income:
        res += f'<div>\n<p>{i.date_of_income}</p>\n<p>{i.amount_of_income}</p>\n</div>\n<hr>\n'
    return HttpResponse(res)


def test(request):
    return HttpResponse("<h1>Test page</h1>")
