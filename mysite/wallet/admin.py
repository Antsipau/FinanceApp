from django.contrib import admin

from .models import Income
from .models import PurchasedGoods


class IncomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_income', 'amount_of_income')


class PurchasedGoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_purchase', 'name_of_product', 'price_per_item', 'quantity_of_goods',
                    'amount_of_expenses')


admin.site.register(Income, IncomeAdmin)
admin.site.register(PurchasedGoods, PurchasedGoodsAdmin)
