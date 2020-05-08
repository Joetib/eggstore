from decimal import Decimal
from django.conf import settings
from .models import Size, Color, SingleOrder


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        
        
    def add(self, size, color, quantity=1, update_quantity=False):
        product_group = f'{size}:{color}'
        if product_group not in self.cart:
            self.cart[product_group] = {'size': size.size, 'color': color.color,'quantity': 0, 'price': Size.objects.get(size=size).price}
        if update_quantity:
            self.cart[product_group]['quantity'] = int(quantity)
        else:
            self.cart[product_group]['quantity'] += int(quantity)
        self.save()
    
    def save(self):
        self.session.modified = True

    def remove(self, size, color, quantity=None):
        product_group = f'{size}:{color}'
        if product_group  in self.cart:
            if quantity:
                if quantity < self.cart[product_group]['quantity']:
                    self.cart[product_group]['quantity'] = self.cart[product_group]['quantity'] -quantity
                    self.save()

                    return
            del self.cart[product_group]
            self.save()

    def total_amount(self):
        price = 0
        for key, value in self.cart.items():
            price += int(value['quantity']) * float(value['price'])
        return price

    def total_items(self):
        count = 0
        for _, _ in self.cart.items():
            count += 1
        return count

    def total_items_quantity(self):
        count = 0
        for key, value in self.cart.items():
            count += int(value['quantity'])
        return count
    
    def as_object(self):
        objects = []
        for key, value in self.cart.items():
            try:
                objects.append(
                    SingleOrder(
                        size = Size.objects.get(size=value.get('size')),
                        color = Color.objects.get(color=value.get('color')),
                        quantity = value.get('quantity', 0)
                    )
                )
            except Exception as e:
                print(e) 
        return objects