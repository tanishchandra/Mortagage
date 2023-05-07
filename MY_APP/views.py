from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if pass1!=pass2:
            return HttpResponse("Your password and conform password are not same")
        else:
          my_user=User.objects.create_user(uname,email,pass1)
          my_user.save()
          return redirect('login')
        

    return render(request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None :
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse("Username or Pasword is incorrect!!!")
        
    return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def mortage(request):
    return render(request,'mortage.html')

def index(request):
    return render(request,'index.html')

def currency(request):
    return render(request,'currency.html')

def FAQ(request):
    return render(request,'FAQ.html')

def Ourteam(request):
    return render(request,'our_team.html')

def pawnbrokerage(request):
    return render(request,'pawnbrokerage_system.html')

def contactus(request):
    return render(request,'contact us.html')