from django.urls import path

from .views import *

urlpatterns = [
    path('', main_page, name='home'),
    path('income_page/', income, name='my_income'),
    path('purchased_goods_page/', my_purchased_goods, name='my_purchased_goods'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('add_income_page/', add_income, name='add_income'),
    path('add_purchase_page/', add_purchase, name='add_purchase'),

]
