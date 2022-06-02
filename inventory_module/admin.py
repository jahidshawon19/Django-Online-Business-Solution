from django.contrib import admin

from inventory_module.models import *
# Register your models here.

admin.site.register(Customer)
# admin.site.register(Category)
# admin.site.register(Product)
admin.site.register(Order)
