"""
blogging models
"""

from django.db import models

# Create your models here.

from django.contrib.auth.models import User

# inherits from the django Model class

class Post(models.Model):
    """
    Post
    """
    title=models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date=models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
