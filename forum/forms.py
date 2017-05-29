from django import forms

# Create your models here.

class QuestionPostForm(forms.Form):
    question = forms.CharField(label='Question text', max_length=1000)
    tag = forms.CharField(label='Tags', max_length=200)


class AnswerPostForm(forms.Form):
    answer_text = forms.CharField(label='Answer Text', max_length=1000)
    answer_rate = forms.IntegerField(label='Rate')