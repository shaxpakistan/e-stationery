from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

class UserAdmin(admin.ModelAdmin):
    #fields to display on panell
    list_display = ('name', 'location', 'pub_date', 'owner', 'status')

    #filter
    list_filter = ('location','status')

    #customization of creation form
    fieldsets = (
        ('Profile', {'fields': ('profile',)}),
        ('Owner', {'fields': ('owner',)}),
        ('Stationery info', {'fields':('name', 'location', 'motto', 'status',)}),
        # ('Stationery services', {'fields':('service_name', 'task_type',)}),
        # ('Stationery products', {'fields':('products',)}),
    )
    #search
    # search_fields = ('name', 'location', 'service_name', 'task_type', 'products',)
    search_fields = ('name', 'location',)
    list_ordering = ('name',)
    filter_horizontally = ()

admin.site.register(Stationery, UserAdmin)
admin.site.register([Category, Product, CartItem, Cart, Order, Booking, Location,])