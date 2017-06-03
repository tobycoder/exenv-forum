from django.contrib import admin
from .views import QuestionPost, Comment
# Register your models here.
admin.site.register(QuestionPost)
admin.site.register(Comment)
