from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import QuestionPostForm, AnswerPostForm
from .models import QuestionPost, AnswerPost
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

def QuestionOversight(request):
    query = QuestionPost.objects.all()
    return render(request, 'forum/questions.html', {'query': query})

def add_comment_to_post(request, pk):
    post = get_object_or_404(QuestionPost, pk=pk)
    if request.method == "POST":
        form = AnswerPostForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('view', pk=post.pk)
    else:
        form = AnswerPostForm()
    return render(request, 'forum/thanks.html', {'form': form})