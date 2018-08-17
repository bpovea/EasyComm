from oscar.core.loading import get_class, get_model
from oscarapi import serializers
from EasyCommAPI.serializers import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAdminUser


ProductRecord = get_model('analytics', 'ProductRecord')

class report_products(APIView):
	"""
    Reporte acerca de los productos
    """
	def get(self, request, format=None):
	    report = ProductRecord._default_manager.all()
	    serializer = report_product(report, many=True)
	    return Response(serializer.data)
    