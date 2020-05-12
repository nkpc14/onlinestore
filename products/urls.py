from django.urls import path
from .views import ProductDetailView, ProductListView, product_list, product_detail

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("api/products/", product_list, name="product_api_list"),
    path("api/products/<int:pk>", product_detail, name="product_api_detail"),
]
