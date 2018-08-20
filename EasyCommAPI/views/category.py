from oscarapi.views import product
from oscarapi.serializers import ProductLinkSerializer
from rest_framework import generics
from oscar.core.loading import get_class, get_model
from oscarapi import serializers
from EasyCommAPI.serializers import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

Category = get_model('catalogue', 'Category')

__all__ = (
   'products_categories','category_details',
)



class products_categories(APIView):
    """
    Lista todas los categorias de productos.
    """
    def get(self, request, format=None):
        categorias = Category.objects.all()
        serializer = categorie_serializer(categorias, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        category = Category.objects.create(path=request.POST['description'],depth=1,numchild=0,name= request.POST['name'],description=request.POST['description'])
        id = category.id
        category = category.save()
        return Response("", status=status.HTTP_201_CREATED)
        
class category_details(APIView):

    def get_object(self, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = Category.objects.get(pk=pk)
        serializer = categorie_serializer(category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        category = Category.objects.get(pk=pk)
        serializer = categorie_serializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

