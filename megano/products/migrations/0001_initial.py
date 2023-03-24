# Generated by Django 4.1.7 on 2023-03-23 08:36

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='название')),
                ('price', models.DecimalField(db_index=True, decimal_places=2, default=0, max_digits=10, verbose_name='цена')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='количество')),
                ('fullDescription', models.TextField(default='', verbose_name='полное описание')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('limited_edition', models.BooleanField(default=False, verbose_name='ограниченная серия')),
                ('freeDelivery', models.BooleanField(default=False, verbose_name='бесплатная доставка')),
                ('rating', models.PositiveIntegerField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='catalog.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='', max_length=128, verbose_name='имя')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tags', to='products.product', verbose_name='тэг')),
            ],
            options={
                'verbose_name': 'тэг',
                'verbose_name_plural': 'тэги',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to=products.models.product_image_directory_path, verbose_name='изображение')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'изображение продукта',
                'verbose_name_plural': 'изображения продуктов',
                'ordering': ['pk'],
            },
        ),
        migrations.AddIndex(
            model_name='tag',
            index=models.Index(fields=['name'], name='name_ind'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['price'], name='index'),
        ),
    ]
