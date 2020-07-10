from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json

def json_responce(request):
    d=[
        {'rno':101,'name':'prasanth','marks':[45,55,65,75,85,95],'status':True,'backlogs':None},
        {'rno': 102, 'name': 'aswini', 'marks': [45, 55, 65, 75, 85, 95], 'status': True, 'backlogs': None},
        {'rno': 103, 'name': 'tulasi', 'marks': [45, 55, 65, 75, 85, 95], 'status': True, 'backlogs': None},
        {'rno': 104, 'name': 'gouri', 'marks': [45, 55, 65, 75, 85, 95], 'status': True, 'backlogs': None},
        {'rno': 105, 'name': 'lokesh', 'marks': [45, 55, 65, 75, 85, 95], 'status': True, 'backlogs': None},
        {'rno': 106, 'name': 'murali', 'marks': [45, 55, 65, 75, 85, 95], 'status': True, 'backlogs': None},
    ]
    data=json.dumps(d)
    return HttpResponse(data,content_type='application/json')
    #return render(request,data)