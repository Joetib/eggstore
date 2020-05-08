from django.urls import path

from .views import HomePageView, AboutPageView, add_order, checkout,json_endpoint

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('order/', add_order, name='order'),
    path('checkout/', checkout, name='checkout'),
    path('json/cart/', json_endpoint, name="json_cart"),
]
