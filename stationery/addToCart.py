from django.shortcuts import redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='/signin/')
def addTocartView(request, pk):

    #get product id
    product_id   = pk

    #get product
    product_obj  = Product.objects.get(id = product_id)

    #check if cart exist
    cart_id = request.session.get("cart_id", None)
    
    try:
        if cart_id:
            cart_obj = Cart.objects.get(id = cart_id)
            this_product_in_cart = cart_obj.cartitem_set.filter(product=product_obj)

            #item already exist in cart
            if this_product_in_cart.exists():
                messages.info (request, 'this product is already exist in cart..')

            #new item is added in cart
            else:
                cartitem = CartItem.objects.create(cart = cart_obj, product = product_obj, quantity = 1, rate =  product_obj.item_price, subtotal = product_obj.item_price)
                cart_obj.total += product_obj.item_price
                product_obj.item_available -= 1

                product_obj.save()

                if product_obj.item_available == 0:
                    product_obj.delete()
                cart_obj.save()
                
                messages.success(request, 
                    'product added successfully !'
                    )
                
        else:
            cart_obj = Cart.objects.create(total=0)
            request.session['cart_id'] = cart_obj.id
            cartitem = CartItem.objects.create(cart = cart_obj, product = product_obj, quantity = 1, rate =  product_obj.item_price, subtotal = product_obj.item_price)
            cart_obj.total += product_obj.item_price
            cart_obj.save()
    except:
        messages.error(request,
        'Unidentified error - please contact admin in case it`s still persist .')
    
    return redirect('products_list')