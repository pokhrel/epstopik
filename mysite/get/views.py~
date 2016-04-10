from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
import json
from .models import NewsEvents, Exercise


# Create your views here.

def index(request):
    return HttpResponse('Done!')

def news(request):
    try:
        last = request.GET['last']
    except MultiValueDictKeyError:
        return HttpResponse("")
    data = NewsEvents.objects.filter(id__gte=last)
    news = []
    for d in data:
        news.append({'id':str(d.id),'date':str(d.date),'title_en':d.title_en,'title_ne':d.title_ne,'content_en':d.content_en,'content_ne':content_ne}) 
    data = {'count':str(data.count()),'news':news}
    return HttpResponse(json.dumps(data), content_type='text/plain')

def exercise(request):
    try: 
        last = request.GET['last']
    except (MultiValueDictKeyError):
        last = ""
    try:
        filename = request.GET['filename']
    except (MultiValueDictKeyError):
        filename = ""
    if (last is not  ""):
        data = Exercise.objects.filter(id__gte=last)
        exercise = []
        for d in data:
            exercise.append({'id':str(d.id),'name_en':d.name_en,'name_ne':d.name_ne, 'questions':str(d.questions)})
        data = {'count':str(data.count()),'exercise':exercise}
        return HttpResponse(json.dumps(data), content_type='text/plain') 
    elif (filename is not ""):
        data = Exercise.objects.get(name=filename)
        return HttpResponse(data.filename)
    return HttpResponse("") 
    
