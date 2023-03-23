from pyexpat import model

from django.contrib import admin

from catalog.models import Category
from products.models import Product, ProductImage, Tag, Specification, ProductSpecification, Sale


class ProductImages(admin.TabularInline):
    model = ProductImage


class ProductSpecifications(admin.TabularInline):
    model = ProductSpecification

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "name":
            pk_product = str(request).split('/')[4]
            product = Product.objects.get(pk=pk_product)
            specifications = Specification.objects.filter(category=product.category)
            kwargs["queryset"] = specifications
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'title',
        'price',
        'count',
        'category',
        'limited_edition',
        # 'freeDelivery',
    ]
    list_display_links = ['pk', 'title']
    inlines = [ProductImages, ProductSpecifications]
    list_filter = ['limited_edition', 'freeDelivery', 'rating']
    search_fields = ['title', 'category', 'price']
    # radio_fields = {"category": admin.VERTICAL}
    # raw_id_fields = ['category']
    # list_editable = ['freeDelivery']
    fieldsets = (
        ('О продукте', {
            'fields': ('category', 'title', ('price', 'count', 'rating'))
        }),
        ('Дополнительные параметры', {
            'classes': ('collapse',),
            'fields': ('limited_edition', 'freeDelivery')
        }),
        ('Описание товара', {
            'classes': ('collapse',),
            'fields': ('fullDescription',),
        }),
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.filter(parent__gte=1)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'product']
    list_display_links = ['pk', 'product']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    list_display_links = ['pk', 'name']


class CategoryOfSpecification(admin.TabularInline):
    model = Specification.category.through


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    list_display_links = ['pk', 'name']
    inlines = [CategoryOfSpecification]
    exclude = ['category']


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'product', 'price', 'salePrice']
    list_display_links = ['pk', 'product']
