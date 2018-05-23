from django.shortcuts import render
from django.db import connection
from prokat.models import Category, Product, Type


def base_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    types = Type.objects.all()
    context = {
        'categories': categories,
        'products': products,
        'types': types
    }
    return render(request, 'base.html', context)


def product_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {
        'product': product
    }
    return render(request, 'product.html', context)


'''''''''
def type_l(request, pk):
    types = Type.objects.all()
    return render(request, 'category.html', {'types': types})
    
    
'''''


def prod_list(request, pk):
    products = Product.objects.filter(category=pk)
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'products': products,

    }
    return render(request, 'category.html', context)


