import random

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import Product
from products.serializers import ProductSerializer


class ProductPopularView(APIView):

    def get(self, request):
        products = Product.objects.filter(rating=5).prefetch_related('images')
        for product in products:
            product.categoryName = product.category
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class BannersView(APIView):

    def get(self, request):
        products_tmp = Product.objects.filter(favourite=True).prefetch_related('images')
        if len(products_tmp) > 3:
            products = random.sample(list(products_tmp), 3)
        else:
            products = products_tmp
        serializer = ProductSerializer(products, many=True)
        return Response({'banners': serializer.data})


class ProductDetailView(viewsets.ViewSet):

    def retrieve(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)


class ProductLimitedView(APIView):

    def get(self, request):
        products = Product.objects.filter(limited_edition=True).prefetch_related('images')
        for product in products:
            product.categoryName = product.category
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
