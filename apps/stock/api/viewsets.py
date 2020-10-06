from rest_framework import viewsets
from rest_framework import permissions, authentication
from rest_framework.filters import SearchFilter
from .serializers import ProductSerializer , CategorySerializer, BrandSerializer
from apps.stock.models import Product, Category, Brand

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    # def get_queryset(self):
    #     return Product.objects.filter
    # filter_fields = ['name',]
    # filter_backends = (SearchFilter,)
    # search_fields = ('name',)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer