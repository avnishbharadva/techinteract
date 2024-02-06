from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User

# Create your views here.

def index(request):

    return render(request, 'index.html')

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']
        profile_pic = request.FILES.get('profile_pic')

        if password==password_repeat:
            if User.objects.filter(username=username).exists():
                print("Username Already Taken")
                messages.info(request, 'Username Already Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print("Email Already Taken")
                messages.info(request, 'Email Already Taken')
                return redirect('register')
            else:
                user = User.objects.create(first_name=first_name,last_name=last_name,username=username,email=email,password=password,profile_pic=profile_pic)
                user.save()
                print("User Added Successfully")
                return redirect('/')
        else:
            print("Password Not Matching")
            messages.info(request, 'Password Does not Matching')
            return redirect('register')

    return render(request, 'register.html')

def login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists() and User.objects.filter(password=password).exists():
            print("Login Success")
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')