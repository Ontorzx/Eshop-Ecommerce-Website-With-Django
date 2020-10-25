from django.urls import path
from.import views
urlpatterns = [
    path('',views.Home,name="home"),
    path('about/',views.AboutPage,name="about"),
    path('contact/',views.contact,name="contact"),
    path('Search/',views.SearchView,name="SearchView"),
    path('single/<int:id>/',views.Product_single,name="Product_single"),
    path('SameCatagory/<int:id>/<slug:slug>/',views.SameCatagory,name="SameCatagory"),
  
] 