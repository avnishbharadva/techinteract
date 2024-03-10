# from django.contrib import admin, include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin-tags', views.admin_tags, name="admin_tags"),
    path('udpate-tag/<int:tag_id>', views.update_tag, name="update_tag"),
    path('admin-queries', views.admin_queries, name="admin_queries"),
    path('delete_question/<int:question_id>/<int:user_id>', views.delete_question, name="delete_question"),
    path('admin-responses', views.admin_responses, name="admin_responses"),
    path("delete_response/<int:response_id>/<int:user_id>", views.delete_response, name="delete_response"),
    path("delete_tag/<int:tag_id>", views.delete_tag, name="delete_tag"),
    path('admin-users', views.admin_users, name="admin_users"),
    path('delete_user/<int:user_id>', views.delete_user, name="delete_user"),
    path('admin-feedbacks', views.admin_feedbacks, name="admin_feedbacks"),
    path('delete_feedback/<int:feedback_id>', views.delete_feedback, name="delete_feedback"),
    path('addtag', views.addtag, name="addtag"),
    path('admin-login', views.admin_login, name="admin_login"),
    path('admin-register', views.admin_register, name="admin_register"),
    path('admin_logout', views.admin_logout, name="admin_logout"),
]