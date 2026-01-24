from addpro.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, product, qty=1):
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id] += qty
        else:
            self.cart[product_id] = qty

        self.session.modified = True

    @property
    def get_prods(self):
        return Product.objects.filter(id__in=self.cart.keys())

    @property
    def get_quants(self):
        return self.cart

    def cart_total(self):
        total = 0
        for id, qty in self.cart.items():
            product = Product.objects.get(id=id)
            price = product.sale_price if product.is_sale else product.price
            total += price * qty
        return total

    def clear(self):
        self.session['cart'] = {}
        self.session.modified = True


