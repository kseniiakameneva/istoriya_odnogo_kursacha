from django import forms
from .models import Order



class BookingForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('product', 'name', 'phone', 'comment')

