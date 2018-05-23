from django.shortcuts import render
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
def category_view(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    context = {
        'category': category
    }
    return render(request, 'category.html', context)



def category(request, pk):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})
'''''


def type_l(request, pk):
    types = Type.objects.all()
    return render(request, 'category.html', {'types': types})
