from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.stock.api.viewsets import ProductViewSet


list_actions = { 
    'get': 'list', 
    'post': 'create' 
} 
 
single_actions = { 
    'get': 'retrieve', 
    'put': 'update', 
    'patch': 'partial_update', 
    'delete': 'destroy' 
} 
 
urlpatterns = [ 
    path('', ProductViewSet.as_view(list_actions), name="products"),
    path('<int:pk>', ProductViewSet.as_view(single_actions), name='product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
