from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
text = 'defaulttext'
class QuestionPost(models.Model):
    question = models.TextField()
    title = models.CharField(max_length=500, null=True, blank=True)
    tag = models.CharField(max_length=200)
    file = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(QuestionPost, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

class Registration(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    activate = models.CharField(max_length=200, null=True)
    bday = models.DateField(auto_now_add=False, null=True)
    created_at = models.DateField(auto_now_add=True)
    activated = models.BooleanField(null=False, default=0)