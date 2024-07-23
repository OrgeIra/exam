from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'created', 'updated')
    list_filter = ('created', 'updated')
    list_editable = ('stock',)

admin.site.register(Product, ProductAdmin)
