from rest_framework import serializers

from catalog.models import Category, CategoryImage
from products.models import Tag


class CategoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryImage
        fields = ['src', 'alt']


class SubCategorySerializer(serializers.ModelSerializer):
    image = CategoryImageSerializer(many=False)

    class Meta:
        model = Category
        fields = ['id', 'title', 'image', 'href', 'subcategories']


class CategorySerializer(serializers.ModelSerializer):
    image = CategoryImageSerializer(many=False)
    subcategories = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'image', 'href', 'subcategories']


class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        exclude = ['product']
