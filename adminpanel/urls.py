# from django.contrib import admin, include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin-profile', views.admin_profile, name="admin_profile"),
    path('table', views.table, name="table"),
    path('addtag', views.addtag, name="addtag"),
]