from django.db import models

# Create your models here.

class Users(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.TextField()
    profile_pic = models.ImageField(upload_to='user_profile')
    total_query = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)