from django.urls import path

from .views import *

urlpatterns = [
    path('', main_page),
    path('test_page/', test),
    path('income_page', income),

]
