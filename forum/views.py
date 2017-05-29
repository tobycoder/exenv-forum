from django.shortcuts import render, reverse
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
