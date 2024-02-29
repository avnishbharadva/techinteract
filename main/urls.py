from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name='register'),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('add-post', views.add_post, name="add_post"),
    path('questions', views.view_question, name="view_question"),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
]