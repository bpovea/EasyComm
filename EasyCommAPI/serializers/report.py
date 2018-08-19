from rest_framework import serializers
from oscar.core.loading import get_model
from .product import *

ProductRecord = get_model('analytics', 'ProductRecord')
Order = get_model('order', 'Order')
Basket = get_model('basket', 'Basket')
Basket_line = get_model('basket', 'Line')
Order_line = get_model('order', 'Line')
Partner = get_model('partner', 'Partner')

class partner(serializers.ModelSerializer):
	class Meta:
		model = Partner
		fields = ("name",)

class report_product(serializers.ModelSerializer):
	product = product_detail_serializer()
	class Meta:
		model = ProductRecord
		fields = "__all__"

class order_line(serializers.ModelSerializer):
	product = product_detail_serializer()
	partner = partner()
	class Meta:
		model = Order_line
		fields = ("partner","product","quantity",)

class report_order(serializers.ModelSerializer):
	lines = order_line(many=True)
	class Meta:
		model = Order
		fields = "__all__"