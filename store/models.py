from django.db import models
from registration.models import Client
from stock.models import Product
# Create your models here.

class Order(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_order = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.owner)

class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.product)