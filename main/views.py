from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import *
from adminpanel.models import Tag
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
# Create your views here.

def index(request):

    # queries = Query.objects.select_related('tag','user').all()[:6]
    queries = Query.objects.select_related('tag','user').order_by('-created_at')[:6]
    return render(request, 'index.html', {'queries':queries})

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
        user_id = request.user.id
        query = request.POST['query']
        desc = request.POST['desc']
        tag_id = request.POST['tag']
        tag = Tag.objects.get(id=tag_id)
        print(user_id)
        user = Users.objects.get(id=user_id)
        old_query_counter = user.total_query
        new_query_counter = old_query_counter + 1
        user.total_query = new_query_counter
        user.save()
        que = Query.objects.create(user_id=user_id,query=query,desc=desc,tag_id=tag.id)
        print(que)
        return redirect('add_post')
    else:
        tags = Tag.objects.all()
        return render(request, 'add_post.html',{'tags':tags})
    
def view_question(request):

    queries = Query.objects.select_related('tag','user').all()
    # print(queries[0].tag.id)
    return render(request, 'questions.html', {'queries':queries})

def question_detail(request, question_id):

    query = Query.objects.select_related('tag','user').get(id=question_id)
    res = Response.objects.select_related('user').filter(query_id=question_id)
    # print(query.tag)
    # query = get_object_or_404(Query, id=question_id)
    return render(request, 'question_detail.html', {'query': query,'responses':res})

def all_tags(request):

    tags = Tag.objects.all()
    return render(request, 'tags.html', {'tags':tags})

def tag_detail(request, tag_id):

    queries = Query.objects.select_related('tag','user').filter(tag_id=tag_id)
    # print("Tag by Query : ",queries)
    return render(request, "query_by_tag.html", {'queries': queries})

def add_response(request):

    if request.method == 'POST':
        user_id = request.user.id
        query = request.POST['query']
        response = request.POST['response']
        query_id = request.POST['query']
        query = Query.objects.get(id=query_id)
        # print(user)
        user = Users.objects.get(id=user_id)
        old_response_counter = user.total_response
        new_response_counter = old_response_counter + 1
        user.total_response = new_response_counter
        user.save()
        # print(query)
        res = Response.objects.create(user_id=user_id,query_id=query.id,response=response)
        # print(res)
        return redirect(f'/question/{query_id}')
    else:
        print("Nothing")

def profile(request):

    user_detail = Users.objects.get(id=request.user.id)
    posts = Query.objects.select_related('tag').filter(user_id=request.user.id)
    return render(request, 'my_profile.html', {'user_detail':user_detail,'posts':posts})

def user_points(request, user_id,question_id,res_id):
    user = Users.objects.get(id = user_id)
    response = Response.objects.get(id= res_id)
    old_points = user.points
    if response.is_verified == False:

        new_points = old_points+5
        user.points = new_points
        response.is_verified = True
        user.save()
        response.save()

    return redirect(f'/question/{question_id}')

def become_mentor(request):
    return render(request, 'mentor_form.html')

def add_mentor_detail(request):

    if request.method == 'POST':
        user_id = request.user.id
        phone_number = request.POST['phone_number']
        linkedin_profile = request.POST['linkedin_profile']
        experience = request.POST['experience']
        designation = request.POST['designation']
        introduction = request.POST['introduction']
        domains = request.POST['domains']

        mentor = Mentor.objects.create(user_id=user_id,phone_number=phone_number,linkedin_profile=linkedin_profile,experience=experience,designation=designation,introduction=introduction,domains=domains)

        user = Users.objects.get(id=user_id)
        user.is_mentor = True
        user.save()

        return redirect('profile')
    
def view_mentors(request):

    mentors = Mentor.objects.select_related('user').all()
    return render(request, 'mentors.html', {'mentors':mentors})