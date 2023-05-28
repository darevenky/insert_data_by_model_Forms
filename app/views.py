from django.shortcuts import render

# Create your views here.
from app.forms import *

def insert_topic(request):
    TO=TopicForm()
    d={'TO':TO}

    return render(request,'insert_topic.html',d)

def insert_web(request):
    WO=WebpageForm()
    d={'wo':WO}

    return render(request,'insert_web.html',d)

def insert_access(request):
    AO=AccessForm()
    d={'ao':AO}

    return render(request,'insert_access.html',d)