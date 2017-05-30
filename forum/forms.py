from django import forms
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#Create your models here.

class QuestionPostForm(forms.Form):
    question = forms.CharField(label='Question text', max_length=1000)
    tag = forms.CharField(label='Tags', max_length=200)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

