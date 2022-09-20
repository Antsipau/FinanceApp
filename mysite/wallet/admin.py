from django.contrib import admin

from .models import Income, PurchasedGoods, Category


class IncomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_income', 'amount_of_income', 'type_of_income', 'user')
    list_display_links = ('id', 'date_of_income')
    search_fields = ('date_of_income', 'type_of_income')
    list_filter = ('type_of_income', 'user')
    list_editable = ('amount_of_income', 'type_of_income')


class PurchasedGoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_purchase', 'name_of_product', 'price_per_item', 'quantity_of_goods',
                    'category', 'user')
    list_display_links = ('id', 'date_of_purchase')
    search_fields = ('date_of_purchase', 'name_of_product', 'quantity_of_goods', 'category')
    list_filter = ('name_of_product', 'quantity_of_goods', 'price_per_item', 'category', 'user')
    list_editable = ('name_of_product', 'quantity_of_goods', 'price_per_item')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('title',)


admin.site.register(Income, IncomeAdmin)
admin.site.register(PurchasedGoods, PurchasedGoodsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'E-Wallet'
admin.site.site_header = 'E-Wallet administration '
