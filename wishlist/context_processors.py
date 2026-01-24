from .wishlist import Wishlist

def wishlist(request):
    wishlist = Wishlist(request)
    return {
        'wishlist_count': len(wishlist)
    }
