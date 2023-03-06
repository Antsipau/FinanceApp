from urllib import request

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
        categories = Category.objects.filter(
            purchasedgoods__user__id=user.id
        ).annotate(
            cnt=Count('purchasedgoods'
                      )
        ).filter(
            cnt__gt=0
        )
        cache.set('categories', categories, 10)
    return {"categories": categories}
