from django.urls import path
from.import views
urlpatterns = [
    path('shopcart/<int:id>/',views.Add_to_Shoping_cart,name="Add_to_Shoping_cart"),
    path('shopcart/',views.cart_detials,name="cart_detials"),
    path('cart_delete/<int:id>/',views.cart_delete,name="cart_delete"),

]
