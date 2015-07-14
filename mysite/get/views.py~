from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import NewsEvents

# Create your views here.

def index(request):
    return HttpResponse('Done!')

def news_events(request):

    data = NewsEvents.objects.all()
    newsevents = []
    for d in data:
        newsevents.append({'title':d.title,'content':d.content}) 
    data = {'count':data.count(),'newsevents':newsevents}
    return HttpResponse(json.dumps(data), content_type='text/plain')

def exercise(request):
    return HttpResponse('Pending!')
    
