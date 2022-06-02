
from django.contrib import admin
from stock_module.models import *
# Register your models here.

admin.site.register(Vendor)
admin.site.register(Category)
admin.site.register(Stock)
admin.site.register(StockHistory)
