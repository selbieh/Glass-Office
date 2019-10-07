from rest_framework.routers import DefaultRouter
from django.urls import path, include

from . import views
router=DefaultRouter()
router.register(r'shopcart',views.shopCartModelView,basename='shopcart')
router.register(r'prodctObject',views.prodctObject,basename='prodctObject')


urlpatterns=[
    path('', include(router.urls)),
    ]