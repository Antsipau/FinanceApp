from django.urls import path

from .views import *

urlpatterns = [
    path('', main_page, name='home'),
    path('income_page/', income, name='my_income'),
    path('total_income_page/', my_total_income, name='total_income_page'),
    path('purchased_goods_page/', my_purchased_goods, name='my_purchased_goods'),
    path('add_income_page/', add_income, name='add_income'),
    path('add_purchase_page/', add_purchase, name='add_purchase'),

]
