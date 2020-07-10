from django.shortcuts import render
from django.views.generic import View
from .models import Employee
from datetime import datetime
import json
from django.http import HttpResponse,JsonResponse

class Http_responce(View):
    def get(self,request):
        list_data = Employee.objects.all()
        dict_data = {}
        for x in list_data:
            d1={
                x.idno:{
                'name':x.name,
                'designation':x.designation,
                'salary':x.salary,
                'date_of_join':x.date_of_join.strftime('%d-%m-%y')
                }
            }

            dict_data.update(d1)
        json_data = json.dumps(dict_data)
        return HttpResponse(json_data)


class Json_responce(View):
    def get(self,request):
        list_data = Employee.objects.all()
        dict_data = {}
        for x in list_data:
            d1 = {
                x.idno: {
                    'name': x.name,
                    'designation': x.designation,
                    'salary': x.salary,
                    'date_of_join': x.date_of_join.strftime('%d-%m-%y')
                }
            }

            dict_data.update(d1)
        return JsonResponse(dict_data)