from django.contrib import admin
from .views import QuestionPost, AnswerPost
# Register your models here.
admin.site.register(QuestionPost)
admin.site.register(AnswerPost)