from django import forms
from .models import Order, Product
from django.utils import timezone
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField


class BookingForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('product', 'name', 'phone', 'comment', 'date', 'date_end')


