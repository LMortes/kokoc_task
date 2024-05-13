from django.contrib import admin
from .models import Currency, ExchangeRate


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('char_code', 'name')
    list_display_links = ('char_code', )
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ['char_code']
    list_per_page = 10


@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('currency', 'date', 'value')
    list_display_links = ('currency', )
    ordering = ['currency__char_code']
    list_filter = ('currency', 'date')
    search_fields = ('currency__name', 'date', 'value')
    list_per_page = 10
