from django.urls import path

from .views import *

urlpatterns = [
    path('', main_page),
    path('income_page/', income),
    path('total_income_page/', my_total_income),
    path('purchased_goods_page/', my_purchased_goods),

]
