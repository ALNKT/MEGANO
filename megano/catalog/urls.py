from django.urls import path

from catalog.views import CategoryView

urlpatterns = [
    path("categories/", CategoryView.as_view()),
]
