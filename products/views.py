from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def all_products(request):
    """
    Displays a single product page
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    Displays all products page, includes sorting and search queries
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'products': product,
    }

    return render(request, 'products/products_detail.html', context)