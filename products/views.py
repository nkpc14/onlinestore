from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Product, Manufacturer
from django.http import JsonResponse


# Generic Class Based Views
class ProductDetailView(DetailView):
    model = Product
    template_name = "product/product_detail.html"


class ProductListView(ListView):
    model = Product
    template_name = "product/product_list.html"


# JSON Response REST API List
def product_list(request):
    product = Product.objects.all()
    data = {"products": list(product.values("pk", "name"))}
    response = JsonResponse(data)
    return response


# JSON Response REST API Detail
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {"product": {
            "name": product.name,
            "manufacturer": product.manufacturer.name,
            "description": product.description,
            "photo": product.photo.url,
            "price": product.price,
            "shipping_cost": product.shipping_cost,
            "quality": product.quantity
        }}
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "product not found!"
            }
        }, status=404)
    return response
