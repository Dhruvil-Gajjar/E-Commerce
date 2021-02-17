from django.contrib import admin
from store.models import *


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = ('user', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'state', 'country', 'zipcode',)

    search_fields = ('name',)

    list_display = ('id', 'user', 'first_name', 'last_name', 'email',)

    ordering = ('id',)


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    fields = ('customer', 'order', 'address', 'state', 'country', 'zipcode',)

    search_fields = ('customer',)

    list_display = ('id', 'customer', 'order', 'address', 'state', 'country', 'zipcode',)

    ordering = ('id',)
