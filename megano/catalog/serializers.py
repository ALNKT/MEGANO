from rest_framework import serializers

from catalog.models import Category, CategoryIcons
from products.models import Tag


class CategoryIconsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryIcons
        fields = ['src', 'alt']


class SubCategorySerializer(serializers.ModelSerializer):
    image = CategoryIconsSerializer(many=False, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'image', 'href', 'subcategories']


class CategorySerializer(serializers.ModelSerializer):
    image = CategoryIconsSerializer(many=False, read_only=True)
    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'image', 'href', 'subcategories']


class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        exclude = ['product']


class BannersSerializer(serializers.ModelSerializer):
    price = serializers.StringRelatedField()
    images = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        fields = ['title', 'href', 'price', 'images']
