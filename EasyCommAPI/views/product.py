from oscarapi.views import product
from oscarapi.serializers import ProductLinkSerializer
from rest_framework import generics
from oscar.core.loading import get_class, get_model
from oscarapi import serializers
from EasyCommAPI.serializers import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAdminUser


Selector = get_class('partner.strategy', 'Selector')

__all__ = (
    'ProductList',
    'products_class',
)

Product = get_model('catalogue', 'Product')
ProductClass = get_model('catalogue', 'ProductClass')
Category = get_model('catalogue', 'Category')

class products_class(APIView):
    """
    Lista todas los clases de productos.
    """
    def get(self, request, format=None):
        categorias = ProductClass.objects.all()
        serializer = clase_productos(categorias, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        permission_classes = (IsAdminUser,)
        serializer = clase_productos(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = product_detail_serializer #ProductLinkSerializer
    
    def get_queryset(self):
        """
        Allow filtering on structure so standalone and parent products can
        be selected separately, eg::
            http://127.0.0.1:8000/api/products/?structure=standalone
        or::
            http://127.0.0.1:8000/api/products/?structure=parent
        """
        qs = super(ProductList, self).get_queryset()
        structure = self.request.query_params.get('structure')
        if structure is not None:
            return qs.filter(structure=structure)
        return qs

    def post(self, request, format=None):
        serializer = product_detail_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

