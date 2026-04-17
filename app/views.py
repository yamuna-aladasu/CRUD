from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from .models import Product
from .serializers import Productserializer


class Createlist(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = Productserializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        products=Product.objects.all()
        serializer=Productserializer(products,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
class Productupdate(APIView):
    parser_classes = [MultiPartParser, FormParser]
    def put(self,request,pk):
        product=get_object_or_404(Product,pk=pk)
        serializer=Productserializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class Productdeletion(APIView):
    def delete(self,request,pk):
        product=get_object_or_404(Product,pk=pk)  
        product.delete()  
        return Response(status=status.HTTP_204_NO_CONTENT)
class Productpartialupdate(APIView):
    parser_classes = [MultiPartParser, FormParser]
    def patch(self,request,pk):
        product=get_object_or_404(Product,pk=pk)
        serializer=Productserializer(product,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
class Productview(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=Productserializer
