from django.shortcuts import render
from django.http import HttpResponse


def main_page(request):
    return HttpResponse("It will be main page")


def test(request):
    return HttpResponse("<h1>Test page</h1>")
