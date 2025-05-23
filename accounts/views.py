from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password= request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are logged in.')
            return redirect('home')
        else:
            messages.error(request,'Invalid login credential')
            return redirect('login')

    return render(request, 'accounts/login.html')

def register(request):
    if request.method =='POST':
        firstname= request.POST.get('firstname')
        lastname= request.POST.get('lastname')
        username= request.POST.get('username')
        email= request.POST.get('email')
        password= request.POST.get('password')
        confirm_password= request.POST.get('confirm_password')

        if password == confirm_password :

            if User.objects.filter(username=username).exists():
                messages.error(request,'username already exist !')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email already exist !')
                    return redirect('register')
                else:
                    user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                   
                    user.save()
                    messages.success(request,'you are registered successfully')
                    return redirect('login')
        else:
            messages.error(request,'Password do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,"you are successfully logged in.")
        return redirect('login')
    return redirect('home')