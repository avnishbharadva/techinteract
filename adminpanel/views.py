from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'adminindex.html')

def profile(request):

    return render(request, 'adminprofile.html')

def table(request):

    return render(request, 'admintable.html')