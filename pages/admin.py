from django.contrib import admin

# Register your models here.
from .models import SiteConfiguration, SingleOrder, Order, UniqueFeature, Size, Color


admin.site.register(Size)
admin.site.register(Color)
admin.site.register(SiteConfiguration)
admin.site.register(UniqueFeature)