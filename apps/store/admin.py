from django.contrib import admin
from .models import Order, Item, Status, FormPayment
# Register your models here.

admin.site.register(Order)
admin.site.register(Item)
admin.site.register(Status)
admin.site.register(FormPayment)