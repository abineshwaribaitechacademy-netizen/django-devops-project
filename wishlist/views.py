from django.http import JsonResponse
from django.shortcuts import get_object_or_404,render
from addpro.models import Product
from .wishlist import Wishlist

def wishlist_add(request):
    if request.method == "POST":
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)

        wishlist = Wishlist(request)
        wishlist.add(product)

        return JsonResponse({
            'message': 'Product added to wishlist',
            'qty': len(wishlist)
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)

def wishlist_summary(request):
    wishlist = Wishlist(request)
    products = wishlist.get_prods()
    
    return render(request, 'wishlist_summary.html', {
        'wishlist_products': products
    })
