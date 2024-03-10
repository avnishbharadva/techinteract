from django.shortcuts import render,redirect
from .models import *
from main.models import *
from django.contrib.auth.models import User

# Create your views here.

def index(request):

    return render(request, 'adminindex.html')

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

    responses = Response.objects.select_related('user').all()
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
            else:
                print("PAssword wrong")
        else:
            print("Invalid credentials")

    return render(request, 'admin_login.html')

def admin_register(request):

    return render(request, 'admin_register.html')