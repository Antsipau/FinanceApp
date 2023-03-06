from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import IncomeForm, PurchaseForm, UserRegisterForm, UserLoginForm
from .models import Income, PurchasedGoods, Category
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail


def register(request):
    """Register user and send e-mail"""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_mail('Registration',
                      'Registration complete',
                      'antsipau@gmail.com',
                      [user.email],
                      fail_silently=False)
            login(request, user)
            messages.success(request, f'User {user} have successfully registered')
            return redirect('home')
        else:
            messages.error(request, 'Registration error')
    else:
        form = UserRegisterForm()
    return render(request, 'wallet/registration_page.html', {'form': form, 'title': 'Registration'})


def user_login(request):
    """Login user"""
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'wallet/login.html', {'form': form, 'title': 'Login'})


def user_logout(request):
    """Logout user"""
    logout(request)
    return redirect('home')


def main_page(request):
    """Display home page"""
    return render(request, 'wallet/main_page.html', {'title': 'Home page'})


@login_required
def income(request):
    """Display income page"""
    my_income = Income.objects.filter(user=request.user)
    return render(request, 'wallet/income_page.html', {'my_income': my_income,
                                                       'title': 'My incomes',
                                                       'user_income': Income.user_income(request)})


@login_required
def my_purchased_goods(request):
    """Display purchased goods"""
    my_goods = PurchasedGoods.objects.select_related('category').filter(user=request.user)
    context = {
        'my_goods': my_goods,
        'title': 'Purchased goods',
        'user_expenses': PurchasedGoods.user_expenses(request),
    }

    return render(request, 'wallet/purchased_goods_page.html', context=context)


@login_required
def add_income(request):
    """Add information into Income Model"""
    user = Income(user=request.user)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IncomeForm()
    return render(request, 'wallet/add_income_page.html', {'form': form, 'title': 'Add income'})


@login_required
def add_purchase(request):
    """Add information into PurchasedGoods Model"""
    user = PurchasedGoods(user=request.user)
    if request.method == 'POST':
        form = PurchaseForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PurchaseForm()
    return render(request, 'wallet/add_purchase_page.html', {'form': form, 'title': 'Add purchase'})


@login_required
def get_category(request, category_id):
    """Get category of purchased goods"""
    goods = PurchasedGoods.objects.select_related('category').filter(category_id=category_id, user=request.user)
    category = get_object_or_404(Category, pk=category_id)

    Category.objects.get(pk=category_id)
    return render(request, 'wallet/category.html', {'goods': goods,
                                                    'category_item': category,
                                                    'title': 'Purchased goods'})
