from django.db import models
from adminpanel.models import Tag

# Create your models here.

class Users(models.Model):

    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    username = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=18)
    profile_pic = models.ImageField(upload_to='user_profile')
    points = models.IntegerField(default=0)
    total_query = models.IntegerField(default=0)
    total_response = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Query(models.Model):

    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    query = models.CharField(max_length=200)
    desc = models.TextField(max_length=1000)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Response(models.Model):

    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    response = models.TextField(max_length=1000)
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

class Feedback(models.Model):

    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)