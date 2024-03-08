from django.shortcuts import render,redirect
from .models import Tag
from main.models import *

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