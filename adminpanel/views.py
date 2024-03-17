from django.shortcuts import render,redirect
from .models import *
from main.models import *
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def index(request):

    if request.session.get('admin_logged_in'):
        return render(request, 'adminindex.html')
    else:
        return redirect('admin_login')

def admin_profile(request):

    return render(request, 'adminprofile.html')

def table(request):

    return render(request, 'admintable.html')

def addtag(request):

    tag_name = request.POST['tag_name']
    tag_desc = request.POST['tag_desc']

    tag = Tag.objects.create(tag_name=tag_name, tag_desc=tag_desc)
    tag.save()
    print("Tag Added Successfully")
    return redirect('admin-panel')

def admin_tags(request):

    tags = Tag.objects.all()
    return render(request, 'admin_tags.html', {'tags':tags})

def admin_queries(request):

    queries = Query.objects.select_related('tag','user').all()
    return render(request, 'admin_queries.html', {'queries':queries})

def admin_responses(request):

    responses = Response.objects.select_related('user','query').all()
    return render(request, 'admin_responses.html', {'responses':responses})

def admin_users(request):

    users = Users.objects.all()
    return render(request, 'admin_users.html', {'users':users})

def delete_question(request, question_id,user_id):

    query = Query.objects.get(id=question_id)
    query.delete()
    user = Users.objects.get(id=user_id)
    old_query_counter = user.total_query
    new_query_counter = old_query_counter - 1
    user.total_query = new_query_counter
    user.save()
    return redirect('admin_queries')

def delete_response(request, response_id, user_id):

    response = Response.objects.get(id=response_id)
    response.delete()
    user = Users.objects.get(id=user_id)
    old_response_counter = user.total_response
    new_response_counter = old_response_counter - 1
    user.total_response = new_response_counter
    user.save()
    return redirect('admin_responses')

def delete_user(request, user_id):

    user = Users.objects.get(id=user_id)
    auser = User.objects.get(id=user_id)
    user.delete()
    auser.delete()
    return redirect('admin_users')

def delete_tag(request, tag_id):

    tag = Tag.objects.get(id=tag_id)
    tag.delete()
    return redirect('admin_tags')

def update_tag(request, tag_id):

    tag = Tag.objects.get(id=tag_id)

    if request.method == "POST":

        tag_name = request.POST['tag_name']
        tag_desc = request.POST['tag_desc']

        tag.tag_name = tag_name
        tag.tag_desc = tag_desc
        tag.save()

        return redirect('admin_tags')
    
    return render(request, 'update_tag.html', {'tag':tag})

def admin_feedbacks(request):

    feedbacks = Feedback.objects.all()
    return render(request, 'admin_feedbacks.html', {'feedbacks':feedbacks})

def delete_feedback(request,feedback_id):

    feedback = Feedback.objects.get(id=feedback_id)
    feedback.delete()
    return redirect('admin_feedbacks')

def admin_login(request):

    if request.method == "POST":

        email = request.POST['email']
        password = request.POST['password']

        if Admin.objects.filter(email=email).exists():

            print("email done")
            if Admin.objects.get(email=email).password == password:
                print("Login done")
                request.session['admin_logged_in'] = True
                return redirect('/admin-panel')
            else:
                messages.info(request, 'Password Incorrect')
                print("PAssword wrong")
        else:
            messages.info(request, 'Invalid Credentials')
            print("Invalid credentials")
            return redirect('admin_login')
        
    return render(request, 'admin_login.html')

def admin_register(request):

    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        admin = Admin.objects.create(name=name,email=email,password=password)

        return redirect('admin_register')

    return render(request, 'admin_register.html')

def admin_logout(request):

    del request.session['admin_logged_in']
    return redirect('admin_login')