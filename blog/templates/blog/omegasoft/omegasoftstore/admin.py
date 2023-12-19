from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(HomeDelivery)
admin.site.register(Discount)
admin.site.register(Invoice)
admin.site.register(Bill)
admin.site.register(Supplier)
admin.site.register(OrderList)
