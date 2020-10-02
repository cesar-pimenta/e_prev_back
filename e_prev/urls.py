
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from e_prev import views
from store.views import OrderViewSet, ItemViewSet
from registration.views import ClientViewSet
from stock.views import ProductViewSet


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'items', ItemViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'products', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
