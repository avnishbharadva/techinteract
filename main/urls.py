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
    path('tags', views.all_tags, name='all_tags'),
    path('tag/<int:tag_id>', views.tag_detail, name="tag_detail"),
    path('add_response', views.add_response, name="add_response"),
    path('profile', views.profile, name='profile'),
    path('user_points/<int:user_id>/<int:question_id>/<int:res_id>', views.user_points, name='user_points'),
    path('become-mentor', views.become_mentor, name='become_mentor'),
    path('add_mentor_detail', views.add_mentor_detail, name="add_mentor_detail"),
    path('mentors', views.view_mentors, name='view_mentors'),
    path('dashboard/mentor', views.mentors_dashboard, name='mentors_dashboard'),
    path('dashboard/mentor/schedule', views.mentors_schedule, name='mentors_schedule'),
]