from django.contrib import admin

from products.models import Product, ProductImage, Tag, Specification, ProductSpecification


class ProductImages(admin.TabularInline):
    model = ProductImage


class ProductSpecifications(admin.TabularInline):
    model = ProductSpecification


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'title',
        'price',
        'count',
        'category',
    ]
    list_display_links = ['pk', 'title']
    inlines = [ProductImages, ProductSpecifications]
    list_filter = ['limited_edition', 'freeDelivery', 'favourite', 'rating']
    search_fields = ['title', 'category', 'price']
    fieldsets = (
        ('О продукте', {
            'fields': ('category', 'title', ('price', 'count', 'rating'))
        }),
        ('Дополнительные параметры', {
            'classes': ('collapse',),
            'fields': ('limited_edition', 'freeDelivery', 'favourite')
        }),
        ('Описание товара', {
            'classes': ('collapse',),
            'fields': ('fullDescription',),
        }),
    )



@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'product']
    list_display_links = ['pk', 'product']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    list_display_links = ['pk', 'name']


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    list_display_links = ['pk', 'name']
