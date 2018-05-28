#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.db import connection
from prokat.models import Category, Product, Type
from .forms import BookingForm
from django.views.generic import ListView
from django.db.models import Q
from django.shortcuts import redirect


def base_view(request):
    categories = Category.objects.raw('SELECT * FROM prokat_category ')
    products = Product.objects.raw('SELECT * FROM prokat_product ')
    types = Type.objects.raw('SELECT * FROM prokat_type ')
    context = {
        'categories': categories,
        'products': products,
        'types': types
    }
    return render(request, 'base.html', context)


def prod_list(request, pk):
    # products = Product.objects.filter(category=pk, available=True)
    products = Product.objects.raw(
        "SELECT * FROM prokat_product WHERE (prokat_product.available = 1 AND prokat_product.category_id = %s)", (pk))
    # print(products.query)
    categories = Category.objects.raw('SELECT * FROM prokat_category ')
    context = {
        'categories': categories,
        'products': products,

    }
    return render(request, 'category.html', context)


def rules_view(request):
    return render(request, 'rules.html')


def contact_view(request):
    return render(request, 'contacts.html')


def thankyou_view(request):
    return render(request, 'thankyou.html')


def prod_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'prod_detail.html', {'product': product})


def booking_view(request):
    form = BookingForm(request.POST or None)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return render(request, 'thankyou.html')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})


def get_queryset(request):
    # Получаем не отфильтрованный кверисет всех моделей
    queryset = Product.objects.all()
    q = request.GET.get("q")

    if q != "":
        # Если 'q' в GET запросе, фильтруем кверисет по данным из 'q'
        # products = queryset.filter(Q(title__icontains=q) |
        # Q(type__icontains=q))
        q1=q.title()
        id_type = Type.objects.filter(type__contains=q1)
        categories = Category.objects.raw('SELECT * FROM prokat_category ')
        products = Product.objects.filter(Q(title__contains=q1) | Q(type = id_type ))
            #"SELECT * FROM prokat_product WHERE prokat_product.title LIKE '%%%s%%' OR prokat_product.type_id =%s ", (q, q))
        context = {
            'categories': categories,
            'products': products,
            'q': q
        }
        return render(request, 'place_search.html', context)
    return render(request, 'place_search.html')
