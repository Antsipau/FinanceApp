from django.urls import path

from .views import *

urlpatterns = [
    path('', main_page, name='home'),
    path('income_page/', income, name='my_income'),
    path('total_income_page/', my_total_income, name='total_income_page'),
    path('purchased_goods_page/', my_purchased_goods, name='my_purchased_goods'),

]
