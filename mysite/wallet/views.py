from django.shortcuts import render, redirect, get_object_or_404

from .forms import IncomeForm, PurchaseForm
from .models import Income, PurchasedGoods, Category


def main_page(request):
    """Display home page"""
    return render(request, 'wallet/main_page.html', {'title': 'Home page'})


def income(request):
    """Display income page"""
    my_income = Income.objects.all()
    return render(request, 'wallet/income_page.html', {'my_income': my_income,
                                                       'title': 'My incomes',
                                                       'total_income': Income.my_total_income()})


def my_purchased_goods(request):
    """Display purchased goods"""
    my_goods = PurchasedGoods.objects.all()
    context = {
        'my_goods': my_goods,
        'title': 'Purchased goods',
    }

    return render(request, 'wallet/purchased_goods_page.html', context=context)


def add_income(request):
    """Add information into Income Model"""
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            Income.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = IncomeForm()
    return render(request, 'wallet/add_income_page.html', {'form': form, 'title': 'Add income'})


def add_purchase(request):
    """Add information into PurchasedGoods Model"""
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            PurchasedGoods.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = PurchaseForm()
    return render(request, 'wallet/add_purchase_page.html', {'form': form, 'title': 'Add purchase'})


# def get_category(request, category_id):
#     """Get category of purchased goods"""
#     goods = PurchasedGoods.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'wallet/category.html', {'goods': goods, 'category': category,
#                                                     'title': 'Purchased goods'})

def get_category(request, category_id):
    """Get category of purchased goods"""
    goods = PurchasedGoods.objects.filter(category_id=category_id)
    category = get_object_or_404(Category, pk=category_id)

    Category.objects.get(pk=category_id)
    return render(request, 'wallet/category.html', {'goods': goods,
                                                    'category_item': category,
                                                    'title': 'Purchased goods'})
