# from django.contrib import admin, include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('profile', views.profile, name="profile"),
    path('table', views.table, name="table"),
    path('addtag', views.addtag, name="addtag"),
]