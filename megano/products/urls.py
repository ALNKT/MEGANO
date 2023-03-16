from django.urls import path
from products.views import ProductPopularView, BannersView, ProductDetailView, ProductLimitedView

urlpatterns = [
    path("products/popular/", ProductPopularView.as_view()),
    path("products/limited/", ProductLimitedView.as_view()),
    path("banners/", BannersView.as_view()),
    path("products/<int:pk>/", ProductDetailView.as_view({'get': 'retrieve'})),
]
