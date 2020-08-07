import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.utils.decorators import method_decorator
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from app8.models import ProductModel
from app8.serializer import ProductSerializer


@method_decorator(csrf_exempt,name='dispatch')
class ProductOperations(View):
    def post(self,request):
        b_data = request.body
        strm_data = io.BytesIO(b_data)
        dict_data = JSONParser().parse(strm_data)
        #ProductModel(name=dict_data['name'],quantity=dict_data['quantity'],price=dict_data['price']).save()
        ps = ProductSerializer(data=dict_data)
        if ps.is_valid():
            ps.save()
            message = {'message':'data is saved'}
        else:
            message = {'error':ps.errors}
        json_data = JSONRenderer().render(message)
        return HttpResponse(json_data,content_type='application/json')
    # def get(self,request):
    #     qs = ProductModel.objects.all()
    #     dict_data = json.loads(qs)
    #     json_data = json.dumps(dict_data)
    #     return HttpResponse(json_data,content_type='application/json')