from rest_framework.response import Response
from rest_framework.views import APIView

from app11.models import ProductModel
from app11.serializer import ProductSerializer

class ApiViews(APIView):
    def post(self,request):
        print(request.body)
        return Response(request.data)
    def get(self,request):
        d = {'idno': 101, 'name': 'prasanth', 'designation': 'developer'}
        return Response(d)


class ProductOperations(APIView):
    def get(self,request,product_no=None):
        qs = ProductModel.objects.all()
        ps = ProductSerializer(qs,many=True)
        return Response(ps.data)

    def post(self,request,product_no=None):
        ps = ProductSerializer(data=request.data)
        if ps.is_valid():
            ps.save()
            message = {'message':'Priduct Saved Successfully'}
        else:
            message = {'error':ps.errors}
        return Response(message)


