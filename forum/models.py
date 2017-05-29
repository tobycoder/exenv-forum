from django.db import models

class QuestionPost(models.Model):
    question = models.CharField(max_length=1000)
    tag = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

class AnswerPost(models.Model):
    answer_text = models.CharField(max_length=1000)
    answer_rate = models.IntegerField()
