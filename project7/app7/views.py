from django.core.serializers import serialize
from django.shortcuts import render
from django.views.generic import View
from app7.forms import CourseForm,StudentForm,FacultyForm
from app7.models import Course,Faculty,Student
import json
from django.http import HttpResponse
from app7.models import Course,Student,Faculty

class CourseOperations(View):

    def get(self,request,cid=0):
        if cid == 0:
            qs = Course.objects.all()
            json_data = serialize('json',[qs])
            return HttpResponse(json_data,content_type='application/json')
        else:
            try:
                qs = Course.objects.get(idno=cid)
                json_data = serialize('json',[qs])
            except Course.DoesNotExist:
                json_data = json.dumps({'Error':'there is no such data is there'})
            return HttpResponse(json_data,content_type='application/json')

    def post(self,request):
        binary_data = request.body
        dict_data = json.loads(binary_data)
        #Course(idno=dict_data['idno'],name=dict_data['name'],fee=dict_data['fee']).save()
        cf = CourseForm(dict_data)
        if cf.is_valid():
            cf.save()
            json_data = json.dumps({'message':'data saved into db'})
        else:
            json_data = json.dumps({'Error':cf.errors})
        return HttpResponse(json_data,content_type='application/json')

    def put(self,requset,cid):
        try:
            old_data = Course.objects.get(idno=cid)
            binary_data = requset.body
            dict_data = json.loads(binary_data)
            cf = CourseForm(dict_data,instance=old_data)
            if cf.is_valid():
                cf.save()
                json_data = json.dumps({'status':'data updated'})
            else:
                json_data = json.dumps({'error':cf.errors})
            return HttpResponse(json_data,content_type='application/json')
        except Course.DoesNotExist:
            json_data = json.dumps({'error':'invalid'})
            return HttpResponse(json_data,content_type='application/json')

    def patch(self,request):
        pass

    def delete(self,request,cid):
        try:
            res = Course.objects.get(idno=cid)
            res.delete()
            json_data = json.dumps({'Message':'Success'})
            return HttpResponse(json_data, 'application/json')
        except Course.DoesNotExist:
            json_data = json.dumps({'Error':'Invalid'})
            return HttpResponse(json_data, 'application/json')