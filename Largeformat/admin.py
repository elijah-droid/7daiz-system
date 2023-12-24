from django.contrib import admin
from .models import Roll


class RollAdmin(admin.ModelAdmin):
    list_display = ('Type', 'Price_per_sq_meter')

admin.site.register(Roll, RollAdmin)