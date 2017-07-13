from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect, HttpResponse
from .forms import Validate, Register
from .models import Registration
from django.utils.crypto import get_random_string
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
import datetime
from django.utils import timezone
from django.core.files.base import ContentFile
# Create your views here.
def login(request):
    if request.method == 'POST':
        form = Validate(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            exists = Registration.objects.filter(username=username).exists()
            activated = Registration.objects.filter(username=username, activated=1).exists()
            if activated == True:
                if exists == True:
                    password_exists = Registration.objects.filter(username=username, password=password).exists()
                    if password_exists == True:
                        request.session['username'] = username
                        url = reverse('forum:check')
                        return HttpResponseRedirect(url)
                    else:
                        return HttpResponse('Password incorrect')
                else:
                    return HttpResponse('Username incorrect')
            else:
                return HttpResponse('Account niet geactiveerd!')
    else:
        form = Validate()
        return render(request, 'forum/login.html', context=locals())

def register(request):
    if request.method == 'POST':
        key = get_random_string(length=32)
        form = Register(request.POST)
        if form.is_valid():
            query = Registration.objects.filter(username__iexact=form.cleaned_data['username']).exists()
            if query == True:
                return HttpResponse('Gebruikersnaam bestaat al')
            else:
                form = form.save()
                user_id = form.id
                email = form.email
                form.save()
                query = Registration.objects.filter(id=user_id).update(activate=key)
                url = reverse('forum:mail', args=[user_id, email, key])
            return HttpResponseRedirect(url)
    else:
        key = get_random_string(length=32)
        form = Register()
        return render(request, 'forum/login.html', context=locals())

def logout(request):
    try:
        del request.session['username']
    except:
        pass
    url = reverse('forum:get_index_page')
    return HttpResponseRedirect(url)

def checkpage(request):
    if request.session.has_key('username'):
        return HttpResponseRedirect(reverse('forum:get_index_page'))
    else:
        return HttpResponse('Inloggen mislukt')

def activate(request, id, activation):
    exist = Registration.objects.filter(id=id, activate=activation).exists()
    if exist == True:
        query = Registration.objects.filter(id=id).update(activated=1)
        return render(request, 'forum/activated.html', context=locals())
    else:
        return HttpResponse('Downie')

def mail(request, user_id, email, activate):
    subject, from_email, to = 'Activatiecode Graffitiburners', 'noreply@graffitiburners.nl', email
    text_content = 'This is an important message.'
    html_content = '<p>Leuk dat je je hebt geregistreerd bij Graffitiburners! Om zeker te weten dat jij bent wie je bent, sturen we deze activatiemail. Hieronder zie je een link, die je zal activeren als je er op klikt. Tot snel bij Graffitiburners!</p><br><a href="http://127.0.0.1:8000/forum/activate/{0}/{1}">Klik hier</a>'.format(user_id, activate)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return HttpResponseRedirect('/forum/btdt/')

def btdt(request):
    return render(request, 'forum/checkmail.html', context=locals())