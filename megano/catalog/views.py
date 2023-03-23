import random

from django.core.paginator import Paginator
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.views import APIView

from catalog.models import Category
from catalog.serializers import CategorySerializer, TagsSerializer, BannersSerializer
from products.models import Tag, Product
from products.serializers import ProductSerializer


class CategoryView(APIView):
    """
    Представление для получения категорий товаров
    """

    def get(self, request):
        categories = []
        categories_tmp = Category.objects.filter(parent=None, active=True).prefetch_related('image', 'subcategories')
        for category in categories_tmp:
            subcategories = [subcategory for subcategory in category.subcategories.filter(active=True)]
            categories.append({'id': category.id, 'title': category.title, 'subcategories': subcategories,
                               'href': category.href, 'image': category.image})
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class TagsView(APIView):
    """
    Представление для получения тэгов товаров
    """

    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagsSerializer(tags, many=True)
        return Response(serializer.data)


class BannersView(APIView):
    """
    Представление для получения баннеров главной страницы
    """

    def get(self, request):
        categories = []
        categories_tmp = Category.objects.filter(parent=not None, active=True, favourite=True).prefetch_related('products')
        if len(categories_tmp) > 3:
            categories_tmp = random.sample(list(categories_tmp), 3)
        for category in categories_tmp:
            product = category.products.order_by('price').first()
            product_min_price = product.price
            product_image = product.images
            categories.append({'href': category.href, 'title': category.title, 'price': product_min_price,
                               'images': product_image})
        serializer = BannersSerializer(categories, many=True)
        return Response({'banners': serializer.data})


def sorting_catalog(request):
    """
    Сортировка каталога по входящим параметрам
    :param request: запрос
    :return: продукты в соответствии с сортировкой
    """
    category = request.GET.get('category')

    # Если в запросе приходит category=0, то отображаем товары всех категорий, иначе только товары запрашиваемой категории
    if category != '0':
        catalog = Category.objects.get(pk=category).products
    else:
        catalog = Product.objects
    sort = request.GET.get('sort')
    sortType = request.GET.get('sortType')
    if sortType == 'inc':
        sortType = '-'
    else:
        sortType = ''
    if sort == 'reviews':
        products = catalog.annotate(count_reviews=Count('reviews')).order_by(f'{sortType}count_reviews').\
            prefetch_related('images', 'reviews')
    else:
        products = catalog.order_by(f'{sortType}{sort}').prefetch_related('images', 'reviews')
    return products


def filter_catalog(request):
    """
    Фильтрация каталога по входящим параметрам
    :param request: запрос
    :return: продукты в соответствии с фильтрацией
    """
    filter_name = request.GET
    print(filter_name)


class CatalogView(APIView):
    """
    Представление для получения товаров каталога
    """

    def get(self, request):
        products = sorting_catalog(request)
        paginator = Paginator(products, 8)
        current_page = paginator.get_page(request.GET.get('page'))
        if len(products) % 8 == 0:  # Определяем количество страниц для отображения на сайте
            lastPage = len(products) // 8
        else:
            lastPage = len(products) // 8 + 1
        for product in current_page:
            product.categoryName = product.category
        serializer = ProductSerializer(current_page, many=True)
        return Response({'items': serializer.data, 'currentPage': request.GET.get('page'), 'lastPage': lastPage})
