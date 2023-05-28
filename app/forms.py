from django import forms
from app.models import *

class TopicForm(forms.Form):
    topic_name=forms.CharField(max_length=100)

class WebpageForm(forms.Form):
    topic_name=forms.CharField(max_length=100)
    name=forms.CharField(max_length=100)
    email=forms.EmailField()

class AccessForm(forms.Form):
    name=forms.CharField(max_length=100)
    url=forms.URLField()
    date=forms.DateField()
