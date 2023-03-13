from django.db import models

from catalog.models import Category


def product_image_directory_path(instance: 'ProductImage', filename):
    return f'static/frontend/assets/img/content/home/products/{instance.product.pk}/{filename}'


class Product(models.Model):
    title = models.CharField(max_length=128, verbose_name='название')
    price = models.DecimalField(max_digits=10, db_index=True, decimal_places=2, default=0, verbose_name='цена')
    count = models.PositiveIntegerField(default=0, verbose_name='количество')
    fullDescription = models.TextField(default='', verbose_name='полное описание')
    # description = models.TextField(default='', verbose_name='описание')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='products', verbose_name='категория')
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    slug = models.SlugField(max_length=128, unique=True, verbose_name='url')
    limited_edition = models.BooleanField(default=False, verbose_name='ограниченная серия')
    freeDelivery = models.BooleanField(default=False, verbose_name='бесплатная доставка')
    href = models.CharField(max_length=128)
    reviews = models.PositiveIntegerField()
    rating = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        indexes = [
            models.Index(fields=['price'], name='index')
        ]

    def description(self):
        if len(self.fullDescription) > 50:
            return f'{self.fullDescription[:50]}...'
        return self.fullDescription

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    image = models.FileField(upload_to=product_image_directory_path, verbose_name='изображение')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='продукт')

    class Meta:
        ordering = ["pk"]
        verbose_name = "изображение продукта"
        verbose_name_plural = "изображения продуктов"

    def __str__(self):
        return f'{self.image}'
