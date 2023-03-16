from rest_framework import serializers
from products.models import Product, ProductImage, ProductSpecification


# class ProductImageSerializer(serializers.ModelSerializer):
#     # src = serializers.StringRelatedField()
#
#     class Meta:
#         model = ProductImage
#         fields = ['image']

class SpecificationsSerializer(serializers.ModelSerializer):
    specification_name = serializers.StringRelatedField()
    name = serializers.StringRelatedField()

    class Meta:
        model = ProductSpecification
        exclude = ['id', 'product']


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True)
    description = serializers.StringRelatedField()
    tags = serializers.StringRelatedField(many=True)
    specifications = SpecificationsSerializer(many=True)
    reviews = serializers.StringRelatedField(many=True)
    href = serializers.StringRelatedField()
    photoSrc = serializers.StringRelatedField(many=True)
    categoryName = serializers.StringRelatedField()

    class Meta:
        model = Product
        exclude = ['limited_edition']
