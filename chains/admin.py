from django.contrib import admin
from django.urls import reverse
# from django.utils.safestring import mark_safe (не понадобилось)
from django.utils.html import format_html

from chains.models import Manufacturer, Product


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'country', 'city', 'street', 'house_number', 'supplier', 'debt',
                    'creation_time', 'type', 'supplier_link',)
    list_filter = ('city',)
    list_display_links = ('id', 'supplier_link',)
    list_select_related = True

    # Вариант 1(плохой)
    # def supplier_link(self, obj):
    #     """Ссылка на Поставщика"""
    #     if obj.supplier:
    #         if obj.supplier:
    #             return f'<a href="/admin/chains/manufacturer/{obj.supplier.id}/change/">{obj.supplier.name}</a>'
    # Вариант 2
    def supplier_link(self, obj):
        """Ссылка на Поставщика"""
        if obj.supplier:
            link = reverse("admin:chains_manufacturer_change", args=[obj.supplier.id])
            return format_html('<a href="{}">{}</a>', link, obj.supplier)

    supplier_link.allow_tags = True
    supplier_link.short_description = "Cсылка на поставщика"

    actions = ['clear_debt']

    @admin.action(description='Mark selected manufacturer for clear debt')
    def clear_debt(self, request, queryset):
        """Очистить значение задолженности перед поставщиком."""
        queryset.update(debt=0.00)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product_model', 'release_date')
