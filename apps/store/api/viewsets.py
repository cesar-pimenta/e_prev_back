from django.contrib.auth.models import User, Group
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import permissions, authentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from .serializers import OrderSerializer, ItemSerializer, FormPaymentSerializer, StatusSerializer
from apps.store.models import Order, Item, Status, FormPayment

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    filter_backends = (DjangoFilterBackend, SearchFilter)

    filter_fields = ('owner',)

    search_fields = ('owner', )


    def get_queryset(self):
        return Order.objects.all()

    def list(self, request, *args, **kwargs):

        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):

        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):

        return super().destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):

        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):

        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):

        return super().partial_update(request, *args, **kwargs)

 

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]


class FormPaymentViewSet(viewsets.ModelViewSet):
    queryset = FormPayment.objects.all()
    serializer_class = FormPaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]