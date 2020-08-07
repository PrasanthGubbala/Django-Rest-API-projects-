import io
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from django.views.generic import View
from app9.models import ProductModel,EmployeeModel
from app9.serializer import ProductSerializer,EmployeeSerializer

@method_decorator(csrf_exempt,name='dispatch')
class ProductOperations(View):
    def post(self,request):
        ps = ProductSerializer(data=JSONParser().parse(io.BytesIO(request.body)))
        try:
            if ps.is_valid():
                ps.save()
                message = {'message': 'data saved successfully'}
            else:
                message = {'error': ps.errors}
            return HttpResponse(JSONRenderer().render(message), content_type='application/json')
        except ValidationError:
            message = {'error':'Invalid Input'}
            return HttpResponse(JSONRenderer().render(message), content_type='application/json')

    def get(self,request):
        query_set = ProductModel.objects.all()
        ps = ProductSerializer(query_set, many=True)
        json_data = JSONRenderer().render(ps.data)
        return HttpResponse(json_data,content_type='application/json')


@method_decorator(csrf_exempt,name='dispatch')
class EmployeeOperations(View):
    def post(self,request):
        es = EmployeeSerializer(data=JSONParser().parse(io.BytesIO(request.body)))
        try:
            if es.is_valid():
                es.save()
                message = {'message': 'data saved successfully'}
            else:
                message = {'error': es.errors}
            return HttpResponse(JSONRenderer().render(message), content_type='application/json')
        except ValidationError:
            message = {'error': 'Invalid Input'}
            return HttpResponse(JSONRenderer().render(message), content_type='application/json')

    def get(self,request):
        query_set = EmployeeModel.objects.all()
        es = EmployeeSerializer(query_set, many=True)
        json_data = JSONRenderer().render(es.data)
        return HttpResponse(json_data,content_type='application/json')
