from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class Category(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return str(self.description)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    brand = models.ForeignKey(Brand,blank=True, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
