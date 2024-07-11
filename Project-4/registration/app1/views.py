from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def Homepage(request):
    return render(request, 'homepage.html')

def upload(request):
    if request.method == 'POST':
        if 'profilePic' in request.FILES:
            profile_pic = request.FILES['profilePic']
            request.user.profile_picture = profile_pic
            request.user.save()
            return redirect('homepage')  # Redirect to the homepage or any other page
    return redirect('homepage')

def Signuppage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Password & confirm password are not match !")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')
def Loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            return HttpResponse("Invalid credential !")
        
    return render(request, 'login.html')

def Logoutpage(request):
    logout(request)
    return redirect('login')