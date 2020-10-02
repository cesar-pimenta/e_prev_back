
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from .views import UserViewSet, GroupViewSet
from store.views import OrderViewSet, ItemViewSet
from stock.views import ProductViewSet

from rest_framework.authtoken import views


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'orders', OrderViewSet, basename='list')
router.register(r'items', ItemViewSet) 
router.register(r'products', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
