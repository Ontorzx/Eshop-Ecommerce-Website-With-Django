from django.contrib import admin
from OrderApp.models import ShopCart
# Register your models here.
from OrderApp.models import  ShopCart

class ShopCar(admin.ModelAdmin):
	list_display=['product','user','quantity','price','amount']
	list_filter=['user']

admin.site.register(ShopCart,ShopCar)