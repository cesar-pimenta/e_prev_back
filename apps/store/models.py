from django.db import models
from apps.client.models import Profile
from apps.stock.models import Product
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Status(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = _('Status')
        verbose_name_plural = _('Status')

    def __str__(self):
        return str(self.name)


class FormPayment(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = _('Type Payment')
        verbose_name_plural = _('Types Payments')

    def __str__(self):
        return str(self.name)


class Order(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_order = models.DateField(auto_now=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    form_payment = models.ForeignKey(FormPayment, on_delete=models.CASCADE)
    frete = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return str(self.owner.username)


class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = _('Item')
        verbose_name_plural = _('Itens')

    def __str__(self):
        return str(self.product)

