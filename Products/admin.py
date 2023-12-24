from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Price', 'Type')


admin.site.register(Product, ProductAdmin)
