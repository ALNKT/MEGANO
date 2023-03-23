from rest_framework import serializers
import locale
from products.models import Product, ProductSpecification, Reviews, Tag, Sale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


class SpecificationsSerializer(serializers.ModelSerializer):
    specification_name = serializers.StringRelatedField()
    name = serializers.StringRelatedField()

    class Meta:
        model = ProductSpecification
        exclude = ['id', 'product']


class ReviewSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format='%d.%m.%Y %H:%M')

    class Meta:
        model = Reviews
        fields = ['author', 'email', 'text', 'rate', 'date', 'product']


class TagsProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True)
    description = serializers.StringRelatedField()
    tags = TagsProductSerializer(many=True)
    specifications = SpecificationsSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    href = serializers.StringRelatedField()
    photoSrc = serializers.StringRelatedField(many=True)
    categoryName = serializers.StringRelatedField()
    price = serializers.DecimalField(source='get_price', max_digits=10, decimal_places=2)

    class Meta:
        model = Product
        exclude = ['limited_edition']




class SaleSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True)
    title = serializers.StringRelatedField()
    href = serializers.StringRelatedField()
    price = serializers.StringRelatedField()
    dateFrom = serializers.DateField(format='%d.%b')
    dateTo = serializers.DateField(format='%d.%b')

    class Meta:
        model = Sale
        fields = '__all__'
