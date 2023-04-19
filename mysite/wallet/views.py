from django.contrib import messages
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import update_session_auth_hash
from django.db.models.query_utils import Q
from django.core.paginator import *

from .forms import IncomeForm, PurchaseForm, UserRegisterForm, UserLoginForm, ChangePasswordForm, \
    ResetPasswordForm, PasswordSetForm
from .models import Income, PurchasedGoods, Category
from .tokens import account_activation_token


def activate(request, uidb64, token):
    """Activate user"""
    user = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = user.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('sign_in')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('home')


def activate_email(request, user, to_email):
    """Send email of activation account"""
    mail_subject = "Activate your user account."
    message = render_to_string("wallet/template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f"Dear {user}, please go to you email {to_email} inbox and click on \
                received activation link to confirm and complete the registration. Note: Check your spam folder.")
    else:
        messages.error(request, f"Problem sending email to {to_email}, check if you typed it correctly.")


def register(request):
    """Register user"""
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activate_email(request, user, form.cleaned_data.get('email'))
            return redirect('home')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

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


def change_password(request):
    """Change password for user"""
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'wallet/change_password.html', {'form': form, 'title': 'Change Password'})


def reset_password(request):
    """Reset password for user"""
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = get_user_model().objects.filter(Q(email=user_email)).first()
            if associated_user:
                subject = "Password Reset request"
                message = render_to_string("wallet/template_reset_password.html", {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'token': account_activation_token.make_token(associated_user),
                    "protocol": 'https' if request.is_secure() else 'http'
                })
                email = EmailMessage(subject, message, to=[associated_user.email])
                if email.send():
                    messages.success(request, """Password reset sent.
                    We've emailed you instructions for setting your password, 
                    if an account exists with the email you entered. 
                    You should receive them shortly. 
                    If you don't receive an email, please make sure you've entered the address 
                    you registered with, and check your spam folder.""")
                else:
                    messages.error(request, "Problem sending reset password email, <b>SERVER PROBLEM</b>")

            return redirect('home')

        for key, error in list(form.errors.items()):
            if key == 'captcha' and error[0] == 'This field is required.':
                messages.error(request, "You must pass the reCAPTCHA test")
                continue

    form = ResetPasswordForm()
    return render(request, 'wallet/reset_password.html', {'form': form, 'title': 'Reset Password'})


def reset_password_confirm(request, uidb64, token):
    """Confirm reset of password"""
    user = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = user.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = PasswordSetForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been set. You may go ahead and log in now.")
                return redirect('home')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = PasswordSetForm(user)
        return render(request, 'wallet/reset_password_confirm.html', {'form': form})
    else:
        messages.error(request, "Link is expired")

    messages.error(request, 'Something went wrong, redirecting back to Homepage')
    return redirect("home")


def main_page(request):
    """Display home page"""
    return render(request, 'wallet/main_page.html', {'title': 'Home page'})


@login_required
def income(request):
    """Display income page"""
    my_income = Income.objects.filter(user=request.user)
    paginator = Paginator(my_income, 5)

    page_number = request.GET.get('page')  # GET параметр page
    my_income = paginator.get_page(page_number)

    return render(request, 'wallet/income_page.html', {'my_income': my_income,
                                                       'title': 'My incomes',
                                                       'total_user_income': Income.total_user_income(request),
                                                       'current_month_income': Income.current_month_income(request),
                                                       'previous_year_income': Income.previous_year_income(request),
                                                       'current_year_income': Income.current_year_income(request),
                                                       'income_difference': Income.income_difference(request)})


@login_required
def my_purchased_goods(request):
    """Display purchased goods"""
    my_goods = PurchasedGoods.objects.select_related('category').filter(user=request.user)
    paginator = Paginator(my_goods, 5)
    page_number = request.GET.get('page')  # GET параметр page
    my_goods = paginator.get_page(page_number)
    context = {
        'my_goods': my_goods,
        'title': 'Purchased goods',
        'user_expenses': PurchasedGoods.user_expenses(request),
        'previous_year_expenses': PurchasedGoods.previous_year_expenses(request),
        'current_month_expenses': PurchasedGoods.current_month_expenses(request),
        'current_year_expenses': PurchasedGoods.current_year_expenses(request),
        'expenses_difference': PurchasedGoods.expenses_difference(request)
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
    paginator = Paginator(goods, 5)
    page_number = request.GET.get('page')  # GET параметр page
    goods = paginator.get_page(page_number)
    category = get_object_or_404(Category, pk=category_id)

    Category.objects.get(pk=category_id)
    return render(request, 'wallet/category.html', {'goods': goods,
                                                    'category_item': category,
                                                    'title': 'Purchased goods'})
