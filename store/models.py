from django.contrib.auth.models import User
from django.db import models
from stock.models import Product
# Create your models here.

class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile")
    date_order = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.id)

class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.product)