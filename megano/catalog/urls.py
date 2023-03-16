from django.urls import path

from catalog.views import CategoryView, TagsView

urlpatterns = [
    path("categories/", CategoryView.as_view()),
    path("tags/", TagsView.as_view()),
]
