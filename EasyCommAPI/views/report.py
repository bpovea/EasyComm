from oscar.core.loading import get_class, get_model
from EasyCommAPI.serializers import *
from rest_framework.views import APIView
from datetime import datetime
from django.db.models import Sum
from django.http import JsonResponse
from reportesMongo.models import *

ReportForm = get_class('dashboard.reports.forms', 'ReportForm')
GeneratorRepository = get_class('dashboard.reports.utils',
                                'GeneratorRepository')

ProductRecord = get_model('analytics', 'ProductRecord')
Order = get_model('order', 'Order')
Order_line = get_model('order', 'Line')
Basket = get_model('basket', 'Basket')
Basket_line = get_model('basket', 'Line')
Product = get_model('catalogue', 'product')

class report_productsNoSQL(APIView):

	def get(self, request, format=None):
		reports = UserReport.objects.all()
		products = {} 
		for usuario in reports:
			for orden in usuario.ordenes:
				for linea in orden.detalle:
					product = Product.objects.get(pk=linea.productID)
					if product.title in products:
						products[product.title] = products[product.title] + linea.cantidad
					else:
						products[product.title] = linea.cantidad
		return JsonResponse({'productos':products},safe=False)

class report_userNoSQL(APIView):

	def get(self, request, format=None):
		reports = UserReport.objects.all()
		usuarios = {} 
		for usuario in reports:
			total = 0.0
			for orden in usuario.ordenes:
				total  = total +orden.total 
			usuarios[usuario.full_name] = total
		return JsonResponse({'usuarios':usuarios},safe=False)

class report_products(APIView):

	def get(self, request, format=None):
		reports = ProductRecord._default_manager.all()
		serializer = report_product(reports, many=True)
		return Response(serializer.data)

class report_orders(APIView):

	def get(self, request, format=None):
		date_from = None
		date_to = None
		orders = Order.objects.all()
		if 'date_from' in request.GET and request.GET['date_from'] != '':
			date_from = request.GET['date_from']
			orders =  orders.filter(date_placed__gte=datetime.strptime(date_from,"%d/%m/%Y"))
		if 'date_to' in request.GET and request.GET['date_to'] != '':
			date_to = request.GET['date_to']
			orders =  orders.filter(date_placed__lte=datetime.strptime(date_to,"%d/%m/%Y"))
		products = {} 

		products_orders = Order_line.objects.filter(order__in=orders)
		for product_order in products_orders:
			if product_order.product.title in products:
				products[product_order.product.title] = products[product_order.product.title] + product_order.quantity
			else:
				products[product_order.product.title] = product_order.quantity
		response = {
			'totales':[
				{'nombre' :'total incluido impuesto','valor': orders.aggregate(Sum('total_incl_tax'))['total_incl_tax__sum']},
				{'nombre' :'total sin incluir impuesto', 'valor': orders.aggregate(Sum('total_excl_tax'))['total_excl_tax__sum']},
				{'nombre' :'entrega incluido impuesto', 'valor': orders.aggregate(Sum('shipping_incl_tax'))['shipping_incl_tax__sum']},
				{'nombre' :'entrega sin incluir impuesto', 'valor': orders.aggregate(Sum('shipping_excl_tax'))['shipping_excl_tax__sum']}
			],
			'productos':products
		}
		return JsonResponse(response,safe=False)

class report_baskets_open(APIView):
	"""docstring for report-baskets-open"""
	def get(self, request, format=None):
		date_from = None
		date_to = None
		baskets = Basket._default_manager.filter(status=Basket.OPEN)
		if 'date_from' in request.GET and request.GET['date_from'] != '':
			date_from = request.GET['date_from']
			baskets =  baskets.filter(date_created__gte=datetime.strptime(date_from,"%d/%m/%Y"))
		if 'date_to' in request.GET and request.GET['date_to'] != '':
			date_to = request.GET['date_to']
			baskets = baskets.filter(date_created__lte=datetime.strptime(date_to,"%d/%m/%Y"))
		products = {} 

		products_baskets = Basket_line.objects.filter(basket__in=baskets)
		for product_basket in products_baskets:
			if product_basket.product.title in products:
				products[product_basket.product.title] = products[product_basket.product.title] + product_basket.quantity
			else:
				products[product_basket.product.title] = product_basket.quantity
		response = {
			'productos':products
		}
		return JsonResponse(response,safe=False)
	
		





