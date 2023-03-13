from django.db import models


def category_image_directory_path(instance: 'CategoryImage', filename):
    if instance.category.parent:
        return f'static/frontend/assets/img/icons/departments/{instance.category.parent}/{instance.category}/{filename}'
    else:
        return f'static/frontend/assets/img/icons/departments/{instance.category}/{filename}'


class Category(models.Model):
    title = models.CharField(max_length=128, db_index=True, verbose_name='название')
    href = models.CharField(max_length=128, blank=True)
    active = models.BooleanField(default=False, verbose_name='активная')
    parent = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True, related_name='subcategories',
                               verbose_name='родитель')

    class Meta:
        ordering = ["title", "pk"]
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.title


class CategoryImage(models.Model):
    alt = models.CharField(max_length=128, blank=True)
    src = models.FileField(upload_to=category_image_directory_path, max_length=500, verbose_name='изображение')
    category = models.OneToOneField(Category, on_delete=models.CASCADE, related_name='image', verbose_name='категория',
                                    blank=True, null=True)

    class Meta:
        ordering = ["pk"]
        verbose_name = "изображение категории"
        verbose_name_plural = "изображения категорий"

    def __str__(self):
        return f'{self.pk}-е изображение'
