from django.urls import path
from .views import *

urlpatterns = [
    path('registration_page/', register, name='registration'),
    path('accounts/login/', user_login, name='sign_in'),
    path('logout_page/', user_logout, name='logout'),
    path('', main_page, name='home'),
    path('income_page/', income, name='my_income'),
    path('purchased_goods_page/', my_purchased_goods, name='my_purchased_goods'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('add_income_page/', add_income, name='add_income'),
    path('add_purchase_page/', add_purchase, name='add_purchase'),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('accounts/change_password', change_password, name='change_password'),
    path('accounts/reset_password', reset_password, name='reset_password'),
    path('reset/<uidb64>/<token>', reset_password_confirm, name='reset_password_confirm'),
]
