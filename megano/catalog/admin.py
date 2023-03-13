from django.contrib import admin
from catalog.models import Category, CategoryImage


class ImageCategory(admin.TabularInline):
    model = CategoryImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ImageCategory]
    list_display = ['pk', 'title', 'href', 'parent', 'active']
    list_display_links = ['pk', 'title']
    list_filter = ['parent', 'active']
    search_fields = ['title']
    ordering = ['parent', 'active']
    actions = ['make_active', 'make_inactive']

    @admin.action(description='Отметить, как активная')
    def make_active(self, request, category):
        updated = category.update(active=True)
        self.message_user(request, message=f'Категорий отмечено АКТИВНОЙ: {updated}')

    @admin.action(description='Отметить, как неактивная')
    def make_inactive(self, request, category):
        updated = category.update(active=False)
        self.message_user(request, message=f'Категорий отмечено НЕАКТИВНОЙ: {updated}')


@admin.register(CategoryImage)
class CategoryImageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'alt', 'category']
    list_display_links = ['pk', 'alt']
