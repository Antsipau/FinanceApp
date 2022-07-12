from django.contrib import admin

from .models import Income
from .models import PurchasedGoods


admin.site.register(Income)
admin.site.register(PurchasedGoods)
