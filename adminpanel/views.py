from django.shortcuts import render,redirect
from .models import Tag

# Create your views here.

def index(request):

    return render(request, 'adminindex.html')

def profile(request):

    return render(request, 'adminprofile.html')

def table(request):

    return render(request, 'admintable.html')

def addtag(request):

    tag_name = request.POST['tag_name']
    tag_desc = request.POST['tag_desc']

    tag = Tag.objects.create(tag_name=tag_name, tag_desc=tag_desc)
    tag.save()
    print("Tag Added Successfully")
    return redirect('profile')