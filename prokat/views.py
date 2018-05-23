from django.shortcuts import render, get_object_or_404
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


def rules_view(request):
    return render(request, 'rules.html')


def prod_detail(request,pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'prod_detail.html', {'product':product})