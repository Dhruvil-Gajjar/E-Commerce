from django.contrib import admin
from store.models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ('customer', 'complete', 'transaction_id',)

    search_fields = ('customer',)

    list_display = ('id', 'customer', 'complete',)

    ordering = ('id',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    fields = ('product', 'order', 'quantity',)

    search_fields = ('product',)

    list_display = ('id', 'product', 'order', 'quantity',)

    ordering = ('id',)
