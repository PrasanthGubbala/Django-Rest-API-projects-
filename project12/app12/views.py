from rest_framework.viewsets import ViewSet
from app12.models import ProductModel
from app12.serializer import ProductSerializer
from rest_framework.response import Response


class ProductOperations(ViewSet):
    def list(self, request):
        qs = ProductModel.objects.all()
        ps = ProductSerializer(qs,many=True)
        return Response(ps.data)


    def create(self, request):
        ps = ProductSerializer(data=request.data)
        if ps.is_valid():
            ps.save()
            message = {'message':'Product Saved Successfully'}
        else:
            message = {'error':ps.errors}
        return Response(message)

    def retrieve(self, request, pk=None):
        try:
            qs = ProductModel.objects.get(pno=pk)
            ps = ProductSerializer(qs)
            return Response(ps.data)
        except ProductModel.DoesNotExist as de:
            return Response({'error':de})

    def update(self, request, pk=None):
        try:
            pd = ProductModel.objects.get(pno=pk)
            ps = ProductSerializer(data=request.data,instance=pd)
            if ps.is_valid():
                ps.save()
                message = {'message':'product is Updated Successfully'}
            else:
                message = {'error':ps.errors}
            return Response(message)
        except ProductModel.DoesNotExist as de:
            return Response({'error': de})


    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        try:
            ProductModel.objects.get(pno=pk).delete()
            message = {'message':'Product Deleted Successfully'}
        except ProductModel.DoesNotExist as de:
            message = {'error':de}
        return Response(message)