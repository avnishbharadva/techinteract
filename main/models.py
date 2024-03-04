from django.db import models
from adminpanel.models import Tag

# Create your models here.

class Users(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.TextField()
    profile_pic = models.ImageField(upload_to='user_profile')
    points = models.IntegerField(default=0)
    total_query = models.IntegerField(default=0)
    total_response = models.IntegerField(default=0)
    is_mentor = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Query(models.Model):

    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    query = models.CharField(max_length=200)
    desc = models.TextField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Response(models.Model):

    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    response = models.TextField()
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    
class Mentor(models.Model):

    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    phone_number = models.BigIntegerField()
    linkedin_profile = models.CharField(max_length=50)
    experience = models.IntegerField(default=0)
    designation = models.TextField(max_length=20)
    introduction = models.CharField(max_length=400)
    domains = models.TextField(max_length=10)