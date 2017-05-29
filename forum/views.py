from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import QuestionPostForm
from .models import QuestionPost
from django.template import RequestContext
from django.utils import timezone
# Create your views here.

def get_question(request):
    if request.method == 'POST':
        form = QuestionPostForm(request.POST)
        if form.is_valid():
            obj = QuestionPost()
            obj.question = form.cleaned_data['question']
            obj.tag = form.cleaned_data['tag']
            obj.created = timezone.now()
            obj.save()
            return render(request, 'forum/thanks.html', {'form': form})
    else:
        form = QuestionPostForm()
    return render(request, 'forum/index.html', {'form': form})

def get_the_text(request, question_url_id):
    query = QuestionPost.objects.filter(pk=question_url_id).values()
    return render(request, 'forum/thanks.html', {'query': query})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def QuestionOversight(request):
    query = QuestionPost.objects.all()
    return render(request, 'forum/questions.html', {'query': query})