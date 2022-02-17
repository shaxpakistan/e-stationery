from django.db.models import fields
from django.forms import ModelForm
from django import forms
from .models import Stationery, Product, Order, Booking

class StationeryForm(forms.ModelForm):
    class Meta:
        model = Stationery
        fields = [
           'name', 'profile', 'location', 'motto' 
        ]

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ('item_name', 'item_desc', 'item_img', 'item_available', 'item_category', 'item_price')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['item_category'].widget.attrs['class'] = 'form-control'
        self.fields['item_available'].widget.attrs['class'] = 'form-control'
        self.fields['item_price'].widget.attrs['class'] = 'form-control'
        self.fields['item_name'].widget.attrs['class'] = 'form-control'
        self.fields['item_desc'].widget.attrs['class'] = 'form-control'
        self.fields['item_img'].widget.attrs['class'] = 'form-control'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["full_name", "email", "phone", "destination"]

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        # fields = '__all__'
        fields = ["file", "service_type", "delivery_mode"]


    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs['class'] = 'form-control'
        self.fields['file'].label = '' 
        self.fields['service_type'].widget.attrs['class'] = 'form-control'
        self.fields['delivery_mode'].widget.attrs['class'] = 'form-control'
