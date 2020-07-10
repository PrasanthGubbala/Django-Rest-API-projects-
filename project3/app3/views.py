from django.shortcuts import render
from django.views.generic import View
import json
from django.http import HttpResponse,JsonResponse

class Http_response(View):
    def get(self,request):
        d1={
            'students_data':[
                {'rno': 101, 'name': 'prasanth', 'marks': [45, 55, 65, 75, 85, 95], 'status': True},
                {'rno': 102, 'name': 'prasanth', 'marks': [45, 55, 65, 75, 85, 95], 'status': True},
                {'rno': 103, 'name': 'prasanth', 'marks': [45, 55, 65, 75, 85, 95], 'status': True},
                {'rno': 104, 'name': 'prasanth', 'marks': [45, 55, 65, 75, 85, 95], 'status': True},
                {'rno': 105, 'name': 'prasanth', 'marks': [45, 55, 65, 75, 85, 95], 'status': True},
                {'rno': 106, 'name': 'prasanth', 'marks': [45, 55, 65, 75, 85, 95], 'status': True}
            ]
        }
        data = json.dumps(d1)
        return HttpResponse(data,content_type='application/json')


class Json_response(View):
    def get(self,request):
        d1 = {
            'students_data': [
                {'rno': 101, 'name': 'prasanth', 'marks': [45, 55, 65, 75, 85, 95], 'status': True},
                {'rno': 102, 'name': 'prasanth', 'marks': [45, 55, 65, 75, 85, 95], 'status': True},
                {'rno': 103, 'name': 'prasanth', 'marks': [45, 55, 65, 75, 85, 95], 'status': True},
                {'rno': 104, 'name': 'prasanth', 'marks': [45, 55, 65, 75, 85, 95], 'status': True},
                {'rno': 105, 'name': 'prasanth', 'marks': [45, 55, 65, 75, 85, 95], 'status': True},
                {'rno': 106, 'name': 'prasanth', 'marks': [45, 55, 65, 75, 85, 95], 'status': True}
            ]
        }
        return JsonResponse(d1)