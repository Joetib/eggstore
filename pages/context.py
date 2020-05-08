from .cart import Cart
from .models import SiteConfiguration
def global_context(request=None)->dict:
    config = SiteConfiguration.object()
    if request:

        cart = Cart(request)
        print(cart.cart)
        return {'cart':cart.as_object(), 'config': config}
    return {'config': 'config'}
        