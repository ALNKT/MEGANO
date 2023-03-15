from django.contrib.auth.models import User
from django.db import models

from catalog.models import Category


def product_image_directory_path(instance: 'ProductImage', filename):
    return f'static/frontend/assets/img/content/home/products/{instance.product.pk}/{filename}'


class Product(models.Model):
    title = models.CharField(max_length=128, verbose_name='название')
    price = models.DecimalField(max_digits=10, db_index=True, decimal_places=2, default=0, verbose_name='цена')
    count = models.PositiveIntegerField(default=0, verbose_name='количество')
    fullDescription = models.TextField(default='', verbose_name='полное описание')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='products', verbose_name='категория')
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    limited_edition = models.BooleanField(default=False, verbose_name='ограниченная серия')
    freeDelivery = models.BooleanField(default=False, verbose_name='бесплатная доставка')
    # reviews = models.PositiveIntegerField()
    rating = models.PositiveIntegerField()
    favourite = models.BooleanField(default=False, verbose_name='избранный товар')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        indexes = [
            models.Index(fields=['price'], name='index')
        ]

    def href(self):
        return f'product/{self.pk}'

    def description(self):
        if len(self.fullDescription) > 50:
            return f'{self.fullDescription[:50]}...'
        return self.fullDescription

    def photoSrc(self):
        return self.images

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    image = models.FileField(upload_to=product_image_directory_path, verbose_name='изображение')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='продукт')

    class Meta:
        ordering = ["pk"]
        verbose_name = "изображение продукта"
        verbose_name_plural = "изображения продуктов"

    def src(self):
        return self.image

    def __str__(self):
        return f'{self.image}'


class Tag(models.Model):
    name = models.CharField(max_length=128, default='', db_index=True, verbose_name='имя')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='tags', verbose_name='тэг')

    class Meta:
        verbose_name = 'тэг'
        verbose_name_plural = 'тэги'

    def __str__(self):
        return self.name


class Specification(models.Model):
    name = models.CharField(max_length=128, default='', verbose_name='название')

    class Meta:
        verbose_name = 'характеристика'
        verbose_name_plural = 'характеристики'

    def __str__(self):
        return self.name


class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='specifications',
                                verbose_name='продукт')
    name = models.ForeignKey(Specification, on_delete=models.PROTECT, related_name='specification_name',
                             verbose_name='название')
    value = models.CharField(max_length=256, default='', verbose_name='значение')

    class Meta:
        verbose_name = 'характеристика продукта'
        verbose_name_plural = 'характеристики продуктов'

    # def __str__(self):
    #     return f'{self.name}'


class Reviews(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', verbose_name='автор')
    email = models.EmailField(max_length=254)
    text = models.TextField(verbose_name='текст')
    rate = models.PositiveSmallIntegerField(blank=False, default=5, verbose_name='оценка')
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='reviews',
                                verbose_name='продукт')

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

    def __str__(self):
        if len(self.text) > 50:
            return f'{self.text[:50]}...'
        return self.text
