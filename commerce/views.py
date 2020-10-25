from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from commerce.models import Setting,ContactMessage,ContactForm
from product.models import Product,Images,Category
from django.http import HttpResponse
from commerce.forms import SearchForm
from OrderApp.models import ShopCart, ShopingCartForm
# Create your views here.
def Home(request):
    current_user = request.user
    cart_product = ShopCart.objects.filter(user_id=current_user.id)
    total_amount=0
    for p in cart_product:
        total_amount += p.product.new_price*p.quantity
    catagory=Category.objects.all()
    setting = Setting.objects.get(id=1)
    slid_images  = Product.objects.all().order_by('-id')[:3]
    latest_product=Product.objects.all().order_by('-id')
    product=Product.objects.all()
    context={
       'slide_images':slid_images,
       'setting': setting,
       'latest_product':latest_product,
       'product':product,
       'catagory':catagory,
       'total_amount':total_amount,
       'cart_product':cart_product,
    }
    return render(request,'commerce/index.html',context)


def Product_single(request,id):
   setting = Setting.objects.get(id=1)
   catagory=Category.objects.all()
   single_product=Product.objects.get(id=id)
   images=Images.objects.filter(product_id=id)
   product=Product.objects.all().order_by('id')[:5]
   context={
      'setting': setting,
      'single_product':single_product,
      'images':images,
      'product':product,
      'catagory':catagory,
      

   }
   return render(request,'commerce/single_product.html',context)

def AboutPage(request):
   setting = Setting.objects.get(id=1)
   catagory=Category.objects.all()
   context={
     'setting': setting,
     'catagory':catagory, 
   }
   return render(request,'commerce/about.html',context)


def SameCatagory(request,id,slug):
   samecat=Product.objects.filter(category_id=id)
   setting = Setting.objects.get(id=1)
   catagory=Category.objects.all()
   slid_images  = Product.objects.all().order_by('-id')[:3]
   context={
      'samecat':samecat,
      'slide_images':slid_images,
      'setting': setting,
      'catagory':catagory,
   }

   return render(request,'commerce/same_cat.html',context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.save()
            messages.success(request, 'Profile details updated.')

            return redirect('contact')

    setting = Setting.objects.get(pk=1)
    form = ContactForm
    catagory=Category.objects.all()
    context = {
        'setting': setting, 'form': form, 'catagory': catagory,
    }
    return render(request, 'commerce/contact_form.html', context)


def SearchView(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            cat_id = form.cleaned_data['cat_id']
            if cat_id == 0:
                products = Product.objects.filter(title__icontains=query)
            else:
                products = Product.objects.filter(
                    title__icontains=query, category_id=cat_id)
            catagory=Category.objects.all()
            slid_images  = Product.objects.all().order_by('-id')[:3]
            setting = Setting.objects.get(id=1)
            context = {
                'catagory':catagory,
                'query': query,
                'samecat': products,
                'slide_images':slid_images,
                'setting': setting,
            }
            return render(request, 'commerce/same_cat.html', context)
    return HttpResponseRedirect('SameCatagory')