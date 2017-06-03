from django import forms
from .models import Comment, QuestionPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#Create your models here.

class QuestionPostForm(forms.ModelForm):

    class Meta:
        model = QuestionPost
        fields = ('title','question', 'tag','file')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

