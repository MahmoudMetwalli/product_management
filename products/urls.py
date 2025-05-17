from django.urls import path
from products.views.api.brand import (
    BrandAPIView, BrandDetailAPIView,
)
from products.views.api.keyword import (
    KeywordAPIView, KeywordDetailAPIView
)
from products.views.api.product import (
    ProductAPIView, ProductDetailAPIView,
)
from products.views.api.search import SearchAPIView
urlpatterns = [
    path('products/', ProductAPIView.as_view(), name='product-list-create'),
    path('products/<uuid:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('brands/', BrandAPIView.as_view(), name='brand-list-create'),
    path('brands/<uuid:pk>/', BrandDetailAPIView.as_view(), name='brand-detail'),
    path('keywords/', KeywordAPIView.as_view(), name='keyword-list-create'),
    path('keywords/<uuid:pk>/', KeywordDetailAPIView.as_view(), name='keyword-detail'),
    path('search/', SearchAPIView.as_view(), name='search-products'),
]
