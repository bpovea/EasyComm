import os
import sys
import django
import random
import requests
import json 

from django_seed import Seed
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EasyComm.settings')
django.setup()

from oscar.core.loading import get_class, get_model
from EasyComm_apps.help import models
from oscar.core.compat import (get_user_model)


User = get_user_model()
Product = get_model('catalogue', 'product')
product_class = get_model('catalogue', 'ProductClass')
category_class = get_model('catalogue', 'Category')
partner_class = get_model('partner', 'Partner')
partner_adress = get_model('partner','PartnerAddress')
country_class = get_model('address', 'Country')
product_category_class = get_model('catalogue', 'ProductCategory')
product_image = get_model('catalogue', 'ProductImage')
partner_stock = get_model('partner', 'StockRecord')
Basket = get_model('basket', 'Basket')

def cambiar_contrasenas():
	for user in User.objects.all():
		user.set_password('a1234567890')
		user.save()

def acortar_nombres():
	for category in category_class.objects.all():
		category.name = category.name[:15]
		category.save()
	for product_clas in product_class.objects.all():
		product_clas.name = product_clas.name[:15]
		product_clas.save()
	for faq in models.Faq.objects.all():
		faq.question=faq.question[0:20]
		faq.answer= faq.answer[0:100]
		faq.save()
def cambiar_lineas_carrito():
	users = User.objects.all()
	for basket in Basket.objects.all():
		basket.owner = users[random.randint(1,len(users)-1)]
		basket.save()

def agregar_carritos_usuarios():
	users = User.objects.all()
	for user in users:
		session = requests.Session()
		if not user.is_staff:
			data = {"username": user.username,"password": 'a1234567890'}
			response = session.post('http://localhost:8000/api/login/', data=data)
			stock = partner_stock.objects.filter(num_in_stock__gte=0)
			for i in range(random.randint(1,4)):
				data = {'url':"http://localhost:8000/api/products/"+ str(stock[random.randint(0,len(stock)-1)].product.id)+ "/" ,"quantity":random.randint(1,2)}
				response = session.post('http://127.0.0.1:8000/api/basket/add-product/',data=data)
				print(response.content)

	#seeder = Seed.seeder()
	#
	#seeder
	#pk = seeder.execute()



#seeder = Seed.seeder()

cantidad = 15
id_fk = 10
id_images = [1,2,3,4,5]
#seeder.add_entity(models.Faq, cantidad)
#seeder.add_entity(product_class, cantidad)
#seeder.add_entity(category_class, cantidad,{'image':  'categories/' + str(random.randint(1,len(id_images))) +.jpg',"depth": 1,"numchild" :0 })
#seeder.add_entity(Product, cantidad,{'product_class':    lambda x: product_class.objects.get(pk=random.randint(1,id_fk)),'parent':lambda x: None})

#seeder.add_entity(partner_class,cantidad)

# no funciona seeder.add_entity(partner_adress,1,{'partner': lambda x: partner_class.objects.get(pk=i),'country':country_class.objects.get(pk='EC')})

#seeder.add_entity(product_category_class, cantidad,{'product':    lambda x: Product.objects.get(pk=random.randint(1,id_fk)),'category':lambda x: category_class.objects.get(pk=random.randint(1,id_fk))})

#seeder.add_entity(product_image,cantidad,{'product':lambda x: Product.objects.get(pk=random.randint(1,id_fk)),'original': lambda x:'images/products/2018/08/' + str(random.randint(1,len(id_images))) +'.jpg'})
#seeder.add_entity(partner_stock,cantidad*2,{'product':lambda x: Product.objects.get(pk=random.randint(1,id_fk)),"price_currency": "DOLLAR",'partner': lambda x: partner_class.objects.get(pk=random.randint(1,id_fk)),"num_in_stock":lambda x: random.randint(0,100)})

#seeder.add_entity(User,cantidad,{'is_staff':random.randint(0,1),'is_active':True,"password": 'a1234567890'})

#pk = seeder.execute()

#acortar_nombres()
#cambiar_contrasenas()

#agregar_carritos_usuarios()
#cambiar_lineas_carrito()


from reportesMongo.models import *

Order = get_model('order', 'Order')
Order_line = get_model('order', 'Line')


def corregirErroresDjangoSeed():
	for stock in partner_stock.objects.all():
		stock.num_allocated = 10
		stock.price_currency = random.randint(0,100)
		stock.cost_price = 10
		stock.num_in_stock = 1000
		stock.low_stock_threshold = 1
		stock.save()

def duplicarorder():
	ordenes = Order.objects.all()

	for orden in ordenes:
		listadetalles = []
		for orden_line in Order_line.objects.filter(order=orden):
			detalle = OrdenDetalle(productID=orden_line.product.id,cantidad=orden_line.quantity)
		listadetalles.append(detalle)
		ors = Orden(codigo=str(orden.id),fecha=orden.date_placed,total=orden.total_incl_tax,detalle=listadetalles)
		user = UserReport(userID=orden.user.id,full_name=str(orden.user.first_name) + " " + str(orden.user.last_name),ordenes=[ors]).save()

#corregirErroresDjangoSeed()

duplicarorder()
