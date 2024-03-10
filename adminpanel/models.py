from django.db import models

# Create your models here.

class Tag(models.Model):

    tag_name = models.CharField(max_length=20)
    tag_desc = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Admin(models.Model):

    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)