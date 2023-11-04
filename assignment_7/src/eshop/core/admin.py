from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(Item)
admin.site.register(Role)
admin.site.register(Order)
admin.site.register(DeliveryData)
admin.site.register(Category)
admin.site.register(Discount)