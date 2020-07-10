from django.shortcuts import render
from django.views.generic import View
from .models import Product
from django.http import HttpResponse,JsonResponse
import json
from django.core.serializers import serialize

class View_all_http_res(View):
    def get(self,request):
        qs = Product.objects.all()
        dict_data = {}
        for x in qs:
            d1 = {
                x.pno:{
                    'product_name':x.name,
                    'quantity':x.quantity,
                    'price':x.price,
                    'mfr_date':x.mfr_date.strftime('%d-%m-%y'),
                    'exp_date':x.exp_date.strftime('%d-%m-%y')
                }
             }
            dict_data.update(d1)
        json_data = json.dumps(dict_data)
        return HttpResponse(json_data,content_type='application/json')

class View_all_json_res(View):
    def get(self,request):
        qs = Product.objects.all()
        dict_data = {}
        for x in qs:
            d1 = {
                x.pno:{
                    'product_name':x.name,
                    'quantity':x.quantity,
                    'price':x.price,
                    'mfr_date':x.mfr_date.strftime('%d-%m-%y'),
                    'exp_date':x.exp_date.strftime('%d-%m-%y')
                }
             }
            dict_data.update(d1)
        return JsonResponse(dict_data)

class View_all_ser(View):
    def get(self,request):
        qs = Product.objects.all()
        json_data = serialize('json', qs)
        return HttpResponse(json_data,content_type='application/json')


class View_one(View):
    def get(self,request,product_no):
        try:
            result = Product.objects.get(pno=product_no)
            dict_data = {
                'product no':result.pno,
                'name':result.name,
                'quantity':result.quantity,
                'price':result.price,
                'mfr_date':result.mfr_date.strftime('%d-%m-%y'),
                'exp_date':result.exp_date.strftime('%d-%m-%y')
            }
        except Product.DoesNotExist:
            dict_data = {'Error':'Invalid Imput'}
        json_data = json.dumps(dict_data)
        return HttpResponse(json_data,content_type='application/json')


class View_one_ser(View):
    def get(self,request,product_no):
        try:
            result = Product.objects.get(pno=product_no)
            json_data = serialize('json',[result])
        except Product.DoesNotExist:
            dict_data = {'Error':'Invalid'}
            json_data = json.dumps(dict_data)
        return HttpResponse(json_data,content_type='application/json')