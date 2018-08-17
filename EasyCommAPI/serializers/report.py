from rest_framework import serializers
from oscar.core.loading import get_model
from .product import *
ProductRecord = get_model('analytics', 'ProductRecord')

class report_product(serializers.ModelSerializer):
	product = product_detail_serializer()
	class Meta:
		model = ProductRecord
		fields = "__all__"
