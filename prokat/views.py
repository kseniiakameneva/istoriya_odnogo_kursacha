from django.shortcuts import render, get_object_or_404
from django.db import connection
from prokat.models import Category, Product, Type
from .forms import BookingForm
from django.shortcuts import redirect


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
    products = Product.objects.filter(category=pk, available=True)
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


def booking_view(request):
    form = BookingForm(request.POST or None)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('prod_detail', pk=product.pk)
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})
