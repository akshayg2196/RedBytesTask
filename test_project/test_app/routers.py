from django.urls import path, include
from rest_framework import routers

from .views import *

# from .APIViews import *

router = routers.DefaultRouter()
router.register("User_reg", user_reg_view, basename='User_reg')
router.register("adminReg", admin_regView, basename='adminReg')
router.register("userReg", user_regView, basename='userReg')
router.register("add_product", add_product_view, basename='add_product')
router.register("cart", cart_view, basename='cart')



urlpatterns = [

    path('', include(router.urls)),

]
