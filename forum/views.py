from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .forms import QuestionPostForm, CommentForm
from .models import QuestionPost, Comment
from django.utils import timezone
from django.core.files.base import ContentFile
# Create your views here.

def get_index_page(request):
    return render(request, 'forum/home.html')

def get_question(request):
    if request.method == 'POST':
        form = QuestionPostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            request_id = form.id
            form.save()
            url = reverse('forum:get_the_text', kwargs={'question_url_id': request_id})
            return HttpResponseRedirect(url)

    else:
        form = QuestionPostForm()
    return render(request, 'forum/index.html', {'form': form})

def get_the_text(request, question_url_id):
    query = QuestionPost.objects.filter(pk=question_url_id).values()
    ifvalue = QuestionPost.objects.filter(pk=question_url_id, file='None').exists()
    querytwo = Comment.objects.filter(post_id=question_url_id)
    return render(request, 'forum/thanks.html', {'query': query, 'querytwo': querytwo, 'ifvalue': ifvalue})

def QuestionOversight(request):
    query = QuestionPost.objects.all()
    return render(request, 'forum/questions.html', {'query': query})

def add_comment_to_post(request, question_url_id):
    post = get_object_or_404(QuestionPost, pk=question_url_id)
    form = CommentForm()
    request_id = question_url_id
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            url = reverse('forum:get_the_text', kwargs={'question_url_id': request_id})
            return HttpResponseRedirect(url)
    else:
        form = CommentForm()
        request_id = question_url_id
    return render(request, 'forum/add_comment_to_post.html', {'form': form, 'request_id': request_id})

def recent_questions(request):
    last_ten = QuestionPost.objects.order_by('created')[:10]
    last_ten_in_ascending_order = reversed(last_ten)
    return render(request, 'forum/recent_post.html', {'last_ten_in_ascending_order': last_ten_in_ascending_order})