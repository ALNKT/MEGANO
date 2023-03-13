from django.urls import path
from products.views import ProductView

urlpatterns = [
    path("products/popular/", ProductView.as_view()),
    # path("products/limited/", ProductView.as_view()),
]
