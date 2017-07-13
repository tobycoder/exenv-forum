"""exenv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views, auth
from django.conf.urls.static import static
from django.conf import settings


admin.autodiscover()
app_name = 'forum'
urlpatterns = [
    url(r'^$', views.get_index_page, name='get_index_page'),
    url(r'^ask/$', views.get_question, name='get_question'),
    url(r'^recent/$', views.recent_questions, name='recent_questions'),
    url(r'^all/$', views.QuestionOversight, name='QuestionOversight'),
    url(r'^view/(?P<question_url_id>[0-9]+)/$', views.get_the_text, name='get_the_text'),
    url(r'^view/(?P<question_url_id>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^login/$', auth.login, name='login'),
    url(r'^register/$', auth.register, name='register'),
    url(r'^logout/$', auth.logout, name='logout'),
    url(r'^check/$', auth.checkpage, name='check'),
    url(r'^activate/(?P<id>[^/?]+)/(?P<activation>[^/?]+)$', auth.activate, name='activate'),
    url(r'^mail/(?P<user_id>[^/?]+)/(?P<email>[^/?]+)/(?P<activate>[^/?]+)/$', auth.mail, name='mail'),
    url(r'^btdt/', auth.btdt, name='btdt'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)