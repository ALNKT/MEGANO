from rest_framework.response import Response
from rest_framework.views import APIView

from catalog.models import Category
from catalog.serializers import CategorySerializer, TagsSerializer
from products.models import Tag


class CategoryView(APIView):

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

    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagsSerializer(tags, many=True)
        return Response(serializer.data)
