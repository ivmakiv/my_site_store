from django.urls import include, path
from rest_framework import routers

from api.views import BasketModelViewSet, ProductModelViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'products', ProductModelViewSet, basename='product-list')
router.register(r'baskets', BasketModelViewSet, basename='basket-list')

urlpatterns = [
    path('', include(router.urls)),
]
