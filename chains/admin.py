from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from chains.models import Manufacturer, Product


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'country', 'city', 'street', 'house_number', 'supplier', 'debt',
                    'creation_time', 'supplier_link',)
    list_filter = ('city',)
    list_display_links = ('id', 'supplier_link',)
    list_select_related = True

    def supplier_link(self, obj):
        """Ссылка на Поставщика"""
        pass

    supplier_link.allow_tags = True
    supplier_link.short_description = "Cсылка на поставщика"

    actions = ['clear_debt']

    @admin.action(description='Mark selected manufacturer for clear debt')
    def clear_debt(self, request, queryset):
        queryset.update(debt=0.00)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product_model', 'release_date')
