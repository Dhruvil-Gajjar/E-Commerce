from django.contrib import admin
from store.models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'price', 'digital', 'image',)

    search_fields = ('name',)

    list_display = ('id', 'name', 'price', 'image',  'digital',)

    ordering = ('id',)

