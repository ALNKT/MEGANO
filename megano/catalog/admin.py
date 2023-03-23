from django.contrib import admin
from catalog.models import Category, CategoryIcons


class ImageCategory(admin.TabularInline):
    model = CategoryIcons


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ImageCategory]
    list_display = ['pk', 'title', 'parent', 'active', 'favourite']
    list_display_links = ['pk', 'title']
    list_filter = ['parent', 'active', 'favourite']
    search_fields = ['title']
    ordering = ['parent', 'active']
    actions = ['make_active', 'make_inactive', 'make_favourite', 'make_not_favourite']

    @admin.action(description='Отметить, как активная')
    def make_active(self, request, category):
        updated = category.update(active=True)
        self.message_user(request, message=f'Категорий отмечено АКТИВНОЙ: {updated}')

    @admin.action(description='Отметить, как неактивная')
    def make_inactive(self, request, category):
        updated = category.update(active=False)
        self.message_user(request, message=f'Категорий отмечено НЕАКТИВНОЙ: {updated}')

    @admin.action(description='Отметить, как избранная')
    def make_favourite(self, request, category):
        updated = category.update(favourite=True)
        self.message_user(request, message=f'Категорий отмечено ИЗБРАННОЙ: {updated}')

    @admin.action(description='Отметить, как неизбранная')
    def make_not_favourite(self, request, category):
        updated = category.update(favourite=False)
        self.message_user(request, message=f'Категорий отмечено НЕИЗБРАННОЕ: {updated}')


@admin.register(CategoryIcons)
class CategoryImageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'alt', 'category']
    list_display_links = ['pk', 'alt']
