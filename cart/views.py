from django.shortcuts import render, redirect
from addpro.models import Product
from django.http import JsonResponse

def cart_summary(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())

    cart_items = []
    for product in products:
        qty = cart[str(product.id)]
        total = product.price * qty
        cart_items.append({
            "product": product,
            "qty": qty,
            "total": total,
        })

    return render(request, "cart/cart_summary.html", {
        "cart_items": cart_items,
    })


def cart_add(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)] += 1
    else:
        cart[str(id)] = 1

    request.session['cart'] = cart
    return redirect("cart_summary")

def cart_delete(request):
    cart = request.session.get('cart', {})

    if request.method == "POST":
        product_id = str(request.POST.get("product_id"))
        print("DELETE:", product_id, cart)   # debug

        if product_id in cart:
            del cart[product_id]

        request.session['cart'] = cart
        return JsonResponse({"success": True})

    return JsonResponse({"success": False})



def cart_update(request):
    cart = request.session.get('cart', {})

    if request.method == "POST":
        product_id = str(request.POST.get("product_id"))
        product_qty = int(request.POST.get("product_qty"))

        if product_id in cart:
            cart[product_id] = product_qty

        request.session['cart'] = cart
        return JsonResponse({"success": True})

    return JsonResponse({"success": False})
