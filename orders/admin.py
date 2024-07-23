from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Order

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('user', 'product', 'quantity', 'status', 'created_at')
    search_fields = ('user__username', 'product__name')
    list_filter = ('status', 'created_at')
    ordering = ('-created_at',)

    class Meta:
        model = Order
