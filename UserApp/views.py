from django.shortcuts import render,redirect
from django.contrib.auth import logout ,authenticate, login
from django.contrib import messages
from commerce.models import Setting,ContactMessage,ContactForm
from product.models import Product,Images,Category
from UserApp.forms import SignUpForm
from UserApp.models import UserProfile
def logout_view(request):
    logout(request)
    messages.warning(request, 'Logout Successfully')
    return redirect('home')


def User_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Your username or password is invalid.')
       
    catagory=Category.objects.all()
    setting = Setting.objects.get(id=1)
    context = {
        'catagory': catagory,
        'setting': setting,
    }
    return render(request,'commerce/user_login.html',context)


def User_registation(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid:
            form.save()
            username=form.cleaned_data.get('username')
            password_raw=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password_raw)
            login(request,user)
            current_user=request.user
            data =UserProfile()
            data.user_id=current_user.id
            data.image="user_img/0I1A0304.JPG"
            data.save()
            messages.warning(request, 'password and confarm passward are not matched.')
            return redirect('home')
        else:
            messages.warning(request, 'password and confarm passward are not matched.')
    else:
        form=SignUpForm
    catagory=Category.objects.all()
    setting = Setting.objects.get(id=1)
    context = {
        'catagory': catagory,
        'setting': setting,
        'form':form,
    }
    return render(request,'commerce/user_sing_up.html',context)
    
def Userprofile(request):
    catagory=Category.objects.all()
    setting = Setting.objects.get(id=1)
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {
        'catagory': catagory,
        'setting': setting,
        'profile':profile,
    }
    return render(request, 'commerce/user_profile.html',context )

