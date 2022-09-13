from django import template
from django.db.models import Count

from wallet.models import Category

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    """Get all categories"""
    return Category.objects.all()


@register.inclusion_tag('wallet/list_categories.html')
def show_categories():
    categories = Category.objects.annotate(cnt=Count('purchasedgoods')).filter(cnt__gt=0)
    return {"categories": categories}
