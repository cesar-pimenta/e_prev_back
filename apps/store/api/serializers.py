from apps.store.models import Order, Item, FormPayment, Status
from apps.stock.api.serializers import ProductSerializer
from rest_framework import serializers


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name']


class FormPaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FormPayment
        fields = ['id', 'name']


class ItemSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = Item
        fields = ['id',]
            

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    item_set = ItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'owner', 'date_order', 'status', 'form_payment', 'frete', 'total','item_set']

