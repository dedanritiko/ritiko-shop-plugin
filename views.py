from django.shortcuts import get_object_or_404, render

from .models import Product


def shop_view(request):
    """Main shop view displaying all products."""
    products = Product.objects.filter(is_active=True)
    context = {"products": products, "title": "Shop"}
    return render(request, "shop.html", context)


def product_detail(request, product_id):
    """Detail view for a single product."""
    product = get_object_or_404(Product, id=product_id, is_active=True)
    context = {"product": product, "title": product.name}
    return render(request, "shop.html", context)
