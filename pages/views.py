from django.views.generic import TemplateView, View
from django.http.response import JsonResponse, Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SingleOrderForm, AddressForm
from .cart import Cart


from .models import Size, Color, Address, Image, UniqueFeature

class HomePageView(View):
    template_name = 'pages/home.html'
    def get(self, request=None, *args, **kwargs):
        images = Image.objects.all()
        sizes = Size.objects.all()
        unique_features = UniqueFeature.objects.all()
        return render(request, 'pages/home.html', {'images': images, 'sizes': sizes, 'unique_features': unique_features})
    


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

def add_order(request):
    if request.method == 'POST':
        order_form = SingleOrderForm(request.POST)
        if order_form.is_valid():
            cd = order_form.cleaned_data
            cart = Cart(request)
            cart.add(cd['size'], cd['color'], cd['quantity'] )
            print('added')
            print(cart.cart, '\n\n')
    else:        
        order_form = SingleOrderForm()
    cart = Cart(request)
    print(cart.cart)
    return render(request, 'pages/add_order.html', {'form': order_form})

@login_required
def checkout(request):
    query_set = Address.objects.filter(user=request.user)
    if query_set.exists():
        user_address = query_set[0]
    else:
        user_address = None
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            query_set = Address.objects.filter(user=request.user)
            if user_address:
                address = form.save(instance=user_address)
            else:
                address = form.save(commit=False)
                address.user = request.user
                address.save()

    form = AddressForm(instance=user_address)
    return render(request, 'pages/checkout.html', {'form': form})

def json_endpoint(request):
    
    qty = int(request.GET.get('qty'))
    size = Size.objects.get(size=request.GET.get('size'))
    color = Color.objects.get(color=request.GET.get('color'))
    if qty and size and color:
        cart = Cart(request)
        cart.add(size, color, quantity=qty, update_quantity=True)
        return JsonResponse({'completed': True, 'qty': qty})
    return JsonResponse({'completed': False})