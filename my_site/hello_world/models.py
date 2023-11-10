from tokenize import Comment
from django.db import models

# Create your models here.

class Member(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class comment(models.Model):
    Comment = models.CharField(max_length=255)