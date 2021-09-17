from django.contrib import admin

# Register your models here.

from . models import Coffee


# @admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'email', 'payment_id', 'paid')
    search_fields = ['name', 'email']
    list_filter = ['amount', 'paid']


admin.site.register(Coffee, CoffeeAdmin)
