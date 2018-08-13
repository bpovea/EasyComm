from rest_framework import serializers
from django.utils.translation import ugettext as _
from oscar.core.loading import get_model
from oscarapi.serializers import *

Product = get_model('catalogue', 'Product')
ProductClass = get_model('catalogue', 'ProductClass')
Category = get_model('catalogue', 'Category')
ProductCategory = get_model('catalogue', 'ProductCategory')
ProductAttribute = get_model('catalogue', 'ProductAttribute')
ProductAttributeValue = get_model('catalogue', 'ProductAttributeValue')
AttributeOption = get_model('catalogue', 'AttributeOption')
ProductImage = get_model('catalogue', 'ProductImage')
Option = get_model('catalogue', 'Option')
Partner = get_model('partner', 'Partner')
StockRecord = get_model('partner', 'StockRecord')

class stock_records(serializers.ModelSerializer):
    class Meta:
        model = StockRecord
        fields = "__all__"

class categoria_productos(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class clase_productos(serializers.ModelSerializer):
    class Meta:
        model = ProductClass
        fields = "__all__"

class producto_imagen(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ("product",) 

class product_detail_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ("attributes","product_options","recommended_products",'categories')    