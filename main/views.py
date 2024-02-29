from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Users,Query
from adminpanel.models import Tag
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
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
            if Users.objects.filter(username=username).exists():
                print("Username Already Taken")
                messages.info(request, 'Username Already Taken')
                return redirect('register')
            elif Users.objects.filter(email=email).exists():
                print("Email Already Taken")
                messages.info(request, 'Email Already Taken')
                return redirect('register')
            else:
                users = Users.objects.create(first_name=first_name,last_name=last_name,username=username,email=email,password=password,profile_pic=profile_pic)
                users.save()
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
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
        username = request.POST['username']
        password = request.POST['password']

        print(username,password)
        user = auth.authenticate(request, username=username, password=password)
        # user = auth.authenticate(request,email=email,password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            print("Login Success")
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
    
def logout(request):

    auth.logout(request)
    return redirect('/')

def add_post(request):

    if request.method == 'POST':
        user = request.user.id
        query = request.POST['query']
        desc = request.POST['desc']
        tag_id = request.POST['tag']
        tag = Tag.objects.get(id=tag_id)
        print(user)
        que = Query.objects.create(user_id=user,query=query,desc=desc,tag_id=tag.id)
        print(que)
        return redirect('add_post')
    else:
        tags = Tag.objects.all()
        return render(request, 'add_post.html',{'tags':tags})
    
def view_question(request):

    queries = Query.objects.select_related('tag','user').all()
    print(queries[0].tag.id)
    return render(request, 'questions.html', {'queries':queries})

def question_detail(request, question_id):
    query = get_object_or_404(Query, id=question_id)
    return render(request, 'question_detail.html', {'query': query})