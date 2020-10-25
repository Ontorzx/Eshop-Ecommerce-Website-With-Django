from django.urls import path
from.import views
urlpatterns = [
    path('registation/',views.User_registation,name="User_registation"),
    path('login/',views.User_login,name="User_login"),
    path('logout/',views.logout_view,name="logout_view"),
    path('Profile/',views.Userprofile,name="UserProfile"),

]
