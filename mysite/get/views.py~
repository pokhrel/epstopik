from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def index(request):
    return HttpResponse('Done!')

def news_events(request):
	"""
	if request.method == 'GET':
		latest = request.GET['latest']
		return HttpResponse("OK. "+latest)
	return HttpResponse("Not cool.")
	"""
	newsevents = []
	newsevents.append({'title':'topic1','content':'this is topic 1 hkjak hakdfkafkasfk jkdhsfkjahs  dkshk  dsakhfka a hkad kasd kahds kasdk asdk kkjah kas hjkaskjf hkj'})
	newsevents.append({'title':'topic2','content':'this is topic 1 hkjak hakdfkafkasfk jkdhsfkjahs  dkshk  dsakhfka a hkad kasd kahds kasdk asdk kkjah kas hjkaskjf hkj'})
	newsevents.append({'title':'topic3','content':'this is topic 1 hkjak hakdfkafkasfk jkdhsfkjahs  dkshk  dsakhfka a hkad kasd kahds kasdk asdk kkjah kas hjkaskjf hkj'})
	newsevents.append({'title':'topic4','content':'this is topic 1 hkjak hakdfkafkasfk jkdhsfkjahs  dkshk  dsakhfka a hkad kasd kahds kasdk asdk kkjah kas hjkaskjf hkj'})
	newsevents.append({'title':'topic5','content':'this is topic 1 hkjak hakdfkafkasfk jkdhsfkjahs  dkshk  dsakhfka a hkad kasd kahds kasdk asdk kkjah kas hjkaskjf hkj'})
	newsevents.append({'title':'topic6','content':'this is topic 1 hkjak hakdfkafkasfk jkdhsfkjahs  dkshk  dsakhfka a hkad kasd kahds kasdk asdk kkjah kas hjkaskjf hkj'})
	newsevents.append({'title':'topic7','content':'this is topic 1 hkjak hakdfkafkasfk jkdhsfkjahs  dkshk  dsakhfka a hkad kasd kahds kasdk asdk kkjah kas hjkaskjf hkj'})
	newsevents.append({'title':'topic8','content':'this is topic 1 hkjak hakdfkafkasfk jkdhsfkjahs  dkshk  dsakhfka a hkad kasd kahds kasdk asdk kkjah kas hjkaskjf hkj'})
	newsevents.append({'title':'topic9','content':'this is topic 1 hkjak hakdfkafkasfk jkdhsfkjahs  dkshk  dsakhfka a hkad kasd kahds kasdk asdk kkjah kas hjkaskjf hkj'})
	newsevents.append({'title':'topic10','content':'this is topic 1 hkjak hakdfkafkasfk jkdhsfkjahs  dkshk  dsakhfka a hkad kasd kahds kasdk asdk kkjah kas hjkaskjf hkj'})
	newsevents.append({'title':'topic11','content':'this is topic 1 hkjak hakdfkafkasfk jkdhsfkjahs  dkshk  dsakhfka a hkad kasd kahds kasdk asdk kkjah kas hjkaskjf hkj'})
	newsevents.append({'title':'topic12','content':'this is topic 1 hkjak hakdfkafkasfk jkdhsfkjahs  dkshk  dsakhfka a hkad kasd kahds kasdk asdk kkjah kas hjkaskjf hkj'})
	newsevents.append({'title':'topic13','content':'this is topic 1 hkjak hakdfkafkasfk jkdhsfkjahs  dkshk  dsakhfka a hkad kasd kahds kasdk asdk kkjah kas hjkaskjf hkj'})
	newsevents.append({'title':'topic14','content':'this is topic 1 hkjak hakdfkafkasfk jkdhsfkjahs  dkshk  dsakhfka a hkad kasd kahds kasdk asdk kkjah kas hjkaskjf hkj'})
	data = {'count':'0','newsevents':newsevents}
	return HttpResponse(json.dumps(data), content_type='aplication/json')
