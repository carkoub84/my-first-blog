from django.shortcuts import render, redirect, HttpResponseRedirect
from django.shortcuts import Products
from django.shortcuts import Category
from django.views import View
 
 
# Create your views here.
class Index(View):
 
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
 
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
 
        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('homepage')
    def get(self, request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')
 