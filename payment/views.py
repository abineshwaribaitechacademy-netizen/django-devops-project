# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from .models import ShippingAddress, Order
# from .forms import ShippingForm, PaymentForm

# from cart.cart import Cart 

# def payment_success(request):
#     return render(request, 'payment_success.html')

# @login_required(login_url='login')
# def checkout(request):
#     cart = Cart(request)
#     shipping_user, created = ShippingAddress.objects.get_or_create(user=request.user)
#     shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
#     return render(request, 'checkout.html', {
#         "cart_products": cart.get_prods,
#         "quantities": cart.get_quants,
#         "totals": cart.cart_total(),
#         "shipping_form": shipping_form
#     })
# def billing_info(request):
#     if request.POST:
#         request.session['my_shipping'] = request.POST  # Store shipping address in session
#         billing_form = PaymentForm()
#         cart = Cart(request)
#         return render(request, 'billing_info.html', {
#             'billing_form': billing_form,
#             'cart_products': cart.get_prods,
#             'quantities': cart.get_quants,
#             'totals': cart.cart_total(),
#             'shipping_info': request.POST
#         })
#     return redirect('home')
# def process_order(request):
#     if request.POST:
#         cart = Cart(request)
#         my_shipping = request.session.get('my_shipping')
#         shipping_address = f"""
#         {my_shipping['shipping_address1']}
#         {my_shipping['shipping_city']}
#         {my_shipping['shipping_state']}
#         {my_shipping['shipping_country']}
#         """

#         if request.user.is_authenticated:
#             order = Order.objects.create(
#                 user=request.user,
#                 full_name=my_shipping['shipping_full_name'],
#                 email=my_shipping['shipping_email'],
#                 shipping_address=shipping_address,
#                 amount_paid=cart.cart_total()
#             )

#         messages.success(request, "Order Placed Successfully!")
#         cart.clear()
#         return redirect('payment_success')

#     messages.error(request, "Invalid Access")
#     return redirect('home')
# from django.contrib.auth.decorators import login_required
# from cart.cart import Cart
# from django.shortcuts import render

# @login_required(login_url='login')
# def checkout(request):
#     cart = Cart(request)  # uses session cart
#     return render(request, 'checkout.html', {
#         'cart_products': cart.get_prods,
#         'quantities': cart.get_quants,
#         'totals': cart.cart_total(),
#     })
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ShippingAddress, Order
from .forms import ShippingForm, PaymentForm
from cart.cart import Cart


def payment_success(request):
    return render(request, 'payment_success.html')


@login_required(login_url='login')
def checkout(request):
    cart = Cart(request)

    # Retrieve or create shipping info for user
    shipping_user, created = ShippingAddress.objects.get_or_create(user=request.user)

    shipping_form = ShippingForm(request.POST or None, instance=shipping_user)

    if request.method == "POST":
        if shipping_form.is_valid():
            shipping_form.save()
            return redirect('billing_info')

    return render(request, 'checkout.html', {
        'cart_products': cart.get_prods,
        'quantities': cart.get_quants,
        'totals': cart.cart_total(),
        'shipping_form': shipping_form,
    })


@login_required(login_url='login')
def billing_info(request):
    cart = Cart(request)

    if request.method == "POST":
        # store shipping info in session
        request.session['my_shipping'] = request.POST
        billing_form = PaymentForm()

        return render(request, 'billing_info.html', {
            'billing_form': billing_form,
            'cart_products': cart.get_prods,
            'quantities': cart.get_quants,
            'totals': cart.cart_total(),
            'shipping_info': request.POST,
        })

    return redirect('checkout')


def process_order(request):
    if request.method == "POST":
        cart = Cart(request)
        my_shipping = request.session.get('my_shipping')

        shipping_address = f"""
        {my_shipping['shipping_address1']}
        {my_shipping['shipping_city']}
        {my_shipping['shipping_state']}
        {my_shipping['shipping_country']}
        """

        order = Order.objects.create(
            user=request.user,
            full_name=my_shipping['shipping_full_name'],
            email=my_shipping['shipping_email'],
            shipping_address=shipping_address,
            amount_paid=cart.cart_total(),
        )

        messages.success(request, "Order Placed Successfully!")
        cart.clear()

        return redirect('payment_success')

    messages.error(request, "Invalid Access")
    return redirect('home')
