from django import forms
from .models import Comment, QuestionPost, Registration
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#Create your models here.

class QuestionPostForm(forms.ModelForm):

    class Meta:
        model = QuestionPost
        fields = ('title','question', 'tag', 'file',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class Validate(forms.ModelForm):

    class Meta:
        model = Registration
        fields = ('username', 'password')

class DateInput(forms.DateInput):
    input_type = 'date'

class Register(forms.ModelForm):

    class Meta:
        model = Registration
        exclude = ('activated','activate')
        widgets = {
            'bday': DateInput(),
        }