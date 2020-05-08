
from django import forms

from .models import SingleOrder, Size, Color, Order, Address
class SingleOrderForm(forms.ModelForm):
    size = forms.ModelChoiceField(queryset=Size.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control w-100'
    }))
    color = forms.ModelChoiceField(queryset=Color.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control w-100'
    }))
    quantity = forms.CharField(widget=forms.NumberInput(attrs={
        'class': 'form-control w-100'
    }))
    class Meta:
        model = SingleOrder
        fields = ( 'size', 'color', 'quantity')

class AddressForm(forms.ModelForm):
    
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control w-100'}))
    house_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control w-100'}))
    street_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control w-100'}))
    town = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control w-100'}))
    region = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control w-100'}))
    class Meta:
        model = Address
        fields = ('phone_number', 'house_number','street_name','town','region', )