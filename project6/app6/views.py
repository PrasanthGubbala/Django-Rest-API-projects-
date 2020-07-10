from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
import json
from app6.forms import ProductForm
from app6.models import Product


class InsertOneItem(View):
    def post(self,request):
        binary_data = request.body
        dict_data = json.loads(binary_data)
        pf = ProductForm(dict_data)
        if pf.is_valid():
            pf.save()
            json_data = json.dumps({'Status':'data saved successfully'})
        else:
            json_data = json.dumps({'Error':pf.errors})

        return HttpResponse(json_data,content_type='application/json')

class DeleteOneItem(View):
    def get(self,request,pno):
        try:
            data = Product.objects.get(pno=pno)
            data.delete()
            json_data = json.dumps({'Message':'Data Deleted Successfully'})
        except Product.DoesNotExist:
            json_data = json.dumps({'Error':'Data Is Not Avalible'})

        return HttpResponse(json_data,content_type='application/json')

class UpdateOneItem(View):
    def post(self,request,pno):
        try:
            old_product = Product.objects.get(pno=pno)
            binary_data = request.body
            dict_data = json.loads(binary_data)
            pf = ProductForm(dict_data,instance=old_product)
            if pf.is_valid():
                pf.save()
                json_data = json.dumps({'Status': 'data saved successfully'})
            else:
                json_data = json.dumps({'Error': pf.errors})

            return HttpResponse(json_data, content_type='application/json')
        except Product.DoesNotExist:
            json_data = json.dumps({'Error':'Invalid'})
            return HttpResponse(json_data, content_type='application/json')
