# wishlist.py
from addpro.models import Product

class Wishlist:
    def __init__(self, request):
        self.session = request.session

        # Check if wishlist exists
        wishlist = self.session.get('session_key_wishlist')

        # If wishlist does NOT exist, create it
        if 'session_key_wishlist' not in request.session:
            wishlist = self.session['session_key_wishlist'] = {}

        self.wishlist = wishlist

    def add(self, product):
        product_id = str(product.id)

        # Add only once — avoids duplicates
        if product_id not in self.wishlist:
            self.wishlist[product_id] = {'product_id': product_id}

        self.session.modified = True  # Save session

    def __len__(self):
        return len(self.wishlist)

    def get_prods(self):
        product_ids = self.wishlist.keys()
        return Product.objects.filter(id__in=product_ids)

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.wishlist:
            del self.wishlist[product_id]
            self.session.modified = True

    def clear(self):
        self.session['session_key_wishlist'] = {}
        self.session.modified = True
