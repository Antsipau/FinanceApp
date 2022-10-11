from django import template
from django.db.models import Count
from django.core.cache import cache

from wallet.models import Category, PurchasedGoods
from django.contrib.auth.models import User
from django.db.models import Q

register = template.Library()


@register.inclusion_tag('wallet/list_categories.html')
def show_categories(user):
    categories = cache.get('categories')
    if not categories:
        categories = Category.objects.annotate(cnt=Count('purchasedgoods', filter=Q(purchasedgoods__user__id=user.id)))
        cache.set('categories', categories, 10)
    return {"categories": categories}
