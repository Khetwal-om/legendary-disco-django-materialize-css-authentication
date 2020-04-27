from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here




def profile(request):
    return render(request,'accounts/profile.html',{})

def home(request):
    return render(request,'index.html',{})


def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('accounts:home')
        else:
            return redirect('accounts:login')

    else:
        return render(request,'accounts/login.html',{})



def register_user(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return redirect('accounts:login')
    else:
         return render(request,'accounts/register.html',{})




def logout_user(request):
    logout(request)
    return redirect('accounts:home')