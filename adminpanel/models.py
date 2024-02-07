from django.db import models

# Create your models here.

class Tag(models.Model):

    tag_name = models.CharField(max_length=100)
    tag_desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)