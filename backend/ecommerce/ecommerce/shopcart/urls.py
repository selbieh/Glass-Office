from rest_framework.routers import DefaultRouter
from . import views
router=DefaultRouter()
router.register('',views.shopCartModelView,basename='userShopCart')

urlpatterns=router.urls