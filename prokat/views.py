from django.shortcuts import render, get_object_or_404
from django.db import connection
from prokat.models import Category, Product, Type
from .forms import BookingForm
from django.shortcuts import redirect
from django.db.models.expressions import RawSQL
from django.db.models.query import QuerySet


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
    #products = Product.objects.filter(category=pk, available=True)
    products = Product.objects.raw("SELECT * FROM prokat_product WHERE (prokat_product.available = 1 AND prokat_product.category_id = %s)",(pk))
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
