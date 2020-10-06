
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from rest_framework import routers

from apps.client.api.viewsets import ProfileViewSet, UserViewSet, GroupViewSet
from apps.store.api.viewsets import OrderViewSet, ItemViewSet, StatusViewSet, FormPaymentViewSet 
from apps.stock.api.viewsets import BrandViewSet, CategoryViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'categorys', CategoryViewSet)
router.register(r'status', StatusViewSet)
router.register(r'formpayments', FormPaymentViewSet)
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'itens', ItemViewSet, basename='item' ) 


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('products/', include('apps.stock.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
