from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class SiteConfiguration(models.Model):
    name = models.CharField(max_length=30)
    icon = models.ImageField(upload_to='icon/', blank=True, null=True)
    banner = models.ImageField(upload_to='banner/', blank=True, null=True)

    def __str__(self):
        return "Site Configuration"

    
    def __repr__(self):
        return "<Site Configuration>"
    
    @classmethod
    def object(cls):
        return cls._default_manager.all().first()


    def save(self):
        self.id = 1
        super(SiteConfiguration, self).save()

class Image(models.Model):
    image = models.ImageField(upload_to='images/')


class UniqueFeature(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.title 

class Size(models.Model):
    size = models.CharField(max_length=20)
    price = models.FloatField()

    def __str__(self):
        return self.size

class Color(models.Model):
    color= models.CharField(max_length=20)
    image = models.ImageField(upload_to="egg/color/", null=True, blank=True)

    def __str__(self):
        return self.color


class Address(models.Model):
    user = models.OneToOneField(User, related_name='address', on_delete=models.CASCADE,)
    phone_number = models.CharField(max_length=13)
    town = models.CharField(max_length=40)
    region = models.CharField(max_length=20)
    street_name = models.CharField(max_length=500)
    house_number = models.CharField(max_length=30)



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    delivered = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    paid_amount = models.FloatField(default=True)
    total_amount = models.FloatField()

    def save(self, *args, **kwargs):
        self.total_amount = sum([single_order.price for single_order in self.single_orders.all()])
        super(Order, self).save(*args, **kwargs)


class SingleOrder(models.Model):
    
    COLOR_CHOICES = (
        ('N', 'None'),
        ('W', 'White'),
        ('B', 'Brown'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="single_orders")
    quantity = models.PositiveIntegerField(default=1)
    size = models.ForeignKey(Size,on_delete=models.CASCADE, related_name="single_orders")
    color = models.ForeignKey(Color,on_delete=models.CASCADE, related_name="single_orders")
   

    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order {self.date_created}'
    


