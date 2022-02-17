from django.contrib.messages.views import SuccessMessageMixin
from django.core.checks import messages
from django.db.models.aggregates import Count
from django.http import request
from django.shortcuts import render, HttpResponse, get_object_or_404, get_list_or_404, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import * 
from .forms import *
from django.urls import reverse_lazy
from django.views import generic
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
import PyPDF2
from PyPDF2 import PdfFileReader
from django.db.models import Sum
class CartTotal(object):
    # displaying total items in cart
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get("cart_id", None)

        user = self.request.user
        try:
            bk_obj = Booking.objects.filter(customer = user)
            total = Booking.objects.filter(customer = user).count()
            context['total'] = total
            context['booking'] = bk_obj
        except:
            context['total'] = 0
            context['booking'] = 0

        if self.request.user.is_authenticated:
            try:
                ct_obj = Cart.objects.get(customer = self.request.user, pk = cart_id)
                total = CartItem.objects.filter(cart = ct_obj).aggregate(Sum('quantity'))['quantity__sum']
                if total is not None:
                    context['total_items'] = total
                else:
                    context['total_items'] = 0
            except:
                context['total_items'] = 0

            if cart_id:
                cart = Cart.objects.get(id=cart_id)
            else:
                cart = None
                context['cart'] = cart
                context['total_items'] = 0

        return context

class CartMixin(object):
    def dispatch(self, request, *args, **kwargs):
        cart_id = request.session.get("cart_id")
        if cart_id:
            cart_obj = Cart.objects.get(id = cart_id)
            if request.user.is_authenticated:
                cart_obj.customer = request.user
                cart_obj.save()

        return super().dispatch(request, *args, **kwargs)

class StationeryRegister(generic.CreateView):
    model = Stationery
    form_class = StationeryForm
    template_name = "stationery/registerstationery.html"
    success_url = reverse_lazy("dashboard")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            pass
        else:
            return redirect("/signin/?next=/register-stationery/")
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        owner = request.user
        if form.is_valid():
            form.instance.owner = owner
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class StationeryDashboard(generic.ListView):
    model = Stationery
    template_name = "stationery/dashboard.html"

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if request.user.is_authenticated and request.user.is_staff:
            pass
        else:
            return redirect("/signin/?next=/dashboard/")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user        
        context['stationery'] = Stationery.objects.filter(owner = user, status = True)
        
        return context

class HomeView(CartTotal, generic.ListView):
    model = Stationery
    ordering = ['pk']
    form = BookingForm
    template_name = "stationery/Home.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['legal'] = Stationery.objects.filter(status = True)
        
        return context     

class DetailsView(CartTotal, CartMixin, generic.DetailView):
    model = Stationery
    template_name = "stationery/stationery_details.html"
    context_object_name = 'detail'


class AddProduct(generic.CreateView):
    model = Product
    form_class = ProductForm
    template_name = "stationery/stationer-dashboard.html"

    def get_success_url(self, **kwargs):
        return reverse('mystationery', kwargs={'pk': self.kwargs['pk']})
    
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if request.user.is_authenticated and request.user.is_staff:
            pass
        else:
            return redirect("/signin/?next=/dashboard/")
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        stat = self.kwargs['pk']
        stat = Stationery.objects.get(name=stat)
        if form.is_valid():
            form.instance.stat_name = stat
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class StationerMixin(object):    
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if request.user.is_authenticated and request.user.is_staff:
            pass
        else:
            return redirect("/signin/?next=/dashboard/")
        return super().dispatch(request, *args, **kwargs)

class Mystationery(StationerMixin, generic.TemplateView):
    model = Stationery
    template_name = "stationery/stationer-dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductForm
        context['stationery'] = Stationery.objects.get(name = self.kwargs['pk'])
        context['prods'] = Product.objects.filter(stat_name = self.kwargs['pk'])
        context['ordersreceiver'] = Order.objects.all()

        return context

class StationeryOrderDetailsView(StationerMixin, generic.TemplateView):
    template_name = "stationery/stationery-order-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stat_id'] = Stationery.objects.get(name=self.kwargs['stat'])
        order_id = self.kwargs['pk']
        our_order = Order.objects.get(id=order_id)
        product_items = Product.objects.all()
        cartitems_found = our_order.cart.cartitem_set.all()
        context['shipping'] = our_order
        zuku = []
        total = []
        idadi = 0
        for item in cartitems_found:
            if item.product.stat_name == context['stat_id']:
                total.append(item.subtotal)
                zuku.append(item)
                idadi += 1

        context['ord_obj'] = zuku
        context['count'] = idadi
        context['zuku_total'] = sum(total)
        return context

class ProductsViews(CartTotal, generic.ListView):
    model = Product
    ordering = ["post_date"]
    template_name = "stationery/products_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['allcategory'] = Category.objects.all()
        return context

class CategoryView(CartTotal, CartMixin, generic.ListView): 
    model = Category
    template_name = "stationery/products_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allcategory'] = get_list_or_404(Category, category_name = self.kwargs['pk'])

        context['category'] = Category.objects.all()
        return context    

class ProductView(CartTotal, CartMixin, generic.TemplateView):
    model = Product
    template_name   = "stationery/product.html"
    # context_object_name = "products"
    success_url = reverse_lazy("item")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statpic'] = get_object_or_404(Stationery, name=self.kwargs['pk'])
        context['stat'] =self.kwargs['pk']
        context["prod"] = Product.objects.filter(stat_name=self.kwargs['pk'])

        return context

class OneProduct(CartTotal, CartMixin, generic.DetailView):
    model = Product
    context_object_name = "item"
    template_name = "stationery/one_product.html"

class StockView(generic.ListView):
    template_name = "stationery/stock.html"
    model = Product
    success_url = reverse_lazy('stock')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stat = self.kwargs["pk"]
        context["jina"] = stat
        context["stock"] = Product.objects.filter(stat_name = stat)
        return context

class StockDetailsView(generic.DetailView):
    model = Product
    context_object_name = "product"
    template_name = "stationery/stock-detail.html"

class StockUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "stationery/stockupdateform.html"

class StockDeleteView(generic.DeleteView):
    model = Product
    template_name = "stationery/stock-detail.html"

    def get_success_url(self):
        return reverse_lazy('stock', kwargs={'pk': self.object.stat_name})

class MyCartView(CartMixin, CartTotal, generic.TemplateView):
    template_name = "stationery/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get("cart_id", None)
        
        if self.request.user.is_authenticated:
            try:
                ct_obj = Cart.objects.get(customer = self.request.user, pk = cart_id)
                total = CartItem.objects.filter(cart = ct_obj).aggregate(Sum('quantity'))['quantity__sum']
                if total is not None:
                    context['total_items'] = total
                else:
                    context['total_items'] = 0
            except:
                context['total_items'] = 0

            if cart_id:
                try:
                    cart = Cart.objects.get(id=cart_id)
                except:
                    context["total_items"] = 0
            else:
                cart = None
            context['cart'] = cart
        return context

class ManageCartView(CartMixin, generic.View):
    def get(self, request, *args, **kwargs):
        cp_id = self.kwargs['cp_id']
        action = request.GET.get("action") 
        cp_obj = CartItem.objects.get(id = cp_id)
        cart_obj = cp_obj.cart
        cart_id = request.session.get("cart_id", None)

        if action == "inc":
            cp_obj.quantity += 1
            cp_obj.subtotal += cp_obj.rate
            cp_obj.save()
            cart_obj.total += cp_obj.rate
            cart_obj.save()

        elif action == "dec":
            cp_obj.quantity -= 1
            cp_obj.subtotal -= cp_obj.rate
            cp_obj.save()
            cart_obj.total -= cp_obj.rate
            cart_obj.save()

            if cp_obj.quantity == 0:
                cp_obj.delete()

        elif action == "rmv":
            cart_obj.total -= cp_obj.subtotal
            cart_obj.save()
            cp_obj.delete()

        else:
            pass


        return redirect("mycart")


class EmptyCartView(CartTotal, CartMixin, generic.View):
    def get(self, request, *args, **kwargs):
        cart_id = request.session.get("cart_id", None)

        if cart_id:
            cart = Cart.objects.get(id = cart_id)
            cart.cartitem_set.all().delete()
            cart.total = 0
            cart.save()
        return redirect("mycart")

class CheckOutView(CartTotal, CartMixin, generic.CreateView):
    template_name = "stationery/checkout.html"
    form_class = OrderForm
    success_url = reverse_lazy("mycart")

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if request.user.is_authenticated:
            pass
        else:
            return redirect("/signin/?next=/checkout/")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get("cart_id", None)

        if cart_id:
            cart_obj = Cart.objects.get(id = cart_id)
        else:
            cart_obj = None 
        context['cart'] = cart_obj
        return context

    def form_valid(self, form):
        cart_id = self.request.session.get("cart_id", None)
        if cart_id:
            cart_obj = Cart.objects.get(id = cart_id)
            form.instance.cart = cart_obj
            form.instance.customer = self.request.user
            form.instance.totalpay = cart_obj.total
            del self.request.session["cart_id"]

        else:
            return redirect("mycart")
        return super().form_valid(form)

class RecordsMix(CartTotal, object):    
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if request.user.is_authenticated:
            pass
        else:
            return redirect("/signin/?next=/records/")
        return super().dispatch(request, *args, **kwargs)

class MyrecordsView(RecordsMix, generic.TemplateView):
    template_name = "stationery/orders.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        us = self.request.user
        context["cust"] = us
        orders = Order.objects.filter(cart__customer = us).order_by("-id")
        context["records"] = orders

        return context

class OrderDetailView(RecordsMix, generic.DetailView):
    model = Order
    context_object_name = "ord"
    template_name = "stationery/orderdetail.html"

class BookingView(CartTotal, generic.CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "stationery/booking.html"
   
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if request.user.is_authenticated:
            pass
        else:
            return redirect("/signin/?next=/")
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse_lazy('stationery_details', kwargs={'pk': self.object.stationery})

    #processing payment for docs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["price"] = 123
        return context


    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        stat_id = self.kwargs['pk']
        stat = Stationery.objects.get(name=stat_id)

        if form.is_valid():
            form.instance.stationery = stat
            form.instance.customer = self.request.user
            form.instance.doc_cost = 500
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class BookingRec(CartTotal, generic.TemplateView):
    model = Booking
    template_name = "stationery/booking-records.html"

    def get_context_data(self, *args, **kwargs):
        context=super().get_context_data(**kwargs)
        try:
            user = self.request.user
            bk_obj = Booking.objects.filter(customer = user).order_by("-id")
            total = Booking.objects.filter(customer = user).count()
            context['total'] = total
            context['booking'] = bk_obj
        except:
            context['total'] = 0
            context['booking'] = 0

        return context

#about us page
class AboutView(CartTotal, generic.TemplateView):
    template_name = "stationery/About.html"

#contact us page
class ContactView(CartTotal, generic.TemplateView):
    template_name = "stationery/Contact.html"
