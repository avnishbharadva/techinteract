# from django.contrib import admin, include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin-tags', views.admin_tags, name="admin_tags"),
    path('admin-queries', views.admin_queries, name="admin_queries"),
    path('admin-responses', views.admin_responses, name="admin_responses"),
    path('admin-users', views.admin_users, name="admin_users"),
    path('addtag', views.addtag, name="addtag"),
]