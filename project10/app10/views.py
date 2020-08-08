import io
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from app10.models import ProductModel
from app10.serializer import ProductSerializer

@method_decorator(csrf_exempt,name='dispatch')
class ProductOperations(View):
    def post(self,request):
        dict_data = JSONParser().parse(io.BytesIO(request.body))
        ps = ProductSerializer(data=dict_data)
        if ps.is_valid():
            ps.save()
            message = {'message':'Product Is Saved'}
        else:
            message = {'error':ps.errors}
        return HttpResponse(JSONRenderer().render(message),content_type='application/json')
    def get(self,request):
        query_set = ProductModel.objects.all()
        ps = ProductSerializer(query_set,many=True)
        return HttpResponse(JSONRenderer().render(ps.data),content_type='application/json')
