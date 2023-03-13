from django.contrib import admin

from products.models import Product, ProductImage


class ProductImages(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'title',
        'price',
        'count',
        'description',
        'category',
    ]
    list_display_links = ['pk', 'title']
    inlines = [ProductImages]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'product']
    list_display_links = ['pk', 'product']
