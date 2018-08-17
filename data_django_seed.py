import os
import sys
import django
import random

from django_seed import Seed
from django.conf import settings
from oscar.core.loading import get_class, get_model
from EasyComm_apps.help import models
from oscar.core.compat import (get_user_model)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EasyComm.settings')
django.setup()

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

#seeder = Seed.seeder()

cantidad = 15
id_fk = 10

#seeder.add_entity(models.Faq, cantidad)
#seeder.add_entity(product_class, cantidad)
#seeder.add_entity(category_class, cantidad,{'image':  'categories/limpieza_oficina.jpg',"depth": 1,"numchild" :0 })
#seeder.add_entity(Product, cantidad,{'product_class':    lambda x: product_class.objects.get(pk=random.randint(1,id_fk)),'parent':lambda x: None})

#seeder.add_entity(partner_class,cantidad)

# no funciona seeder.add_entity(partner_adress,1,{'partner': lambda x: partner_class.objects.get(pk=i),'country':country_class.objects.get(pk='EC')})

#seeder.add_entity(product_category_class, cantidad,{'product':    lambda x: Product.objects.get(pk=random.randint(1,id_fk)),'category':lambda x: category_class.objects.get(pk=random.randint(1,id_fk))})

#seeder.add_entity(product_image,cantidad,{'product':lambda x: Product.objects.get(pk=random.randint(1,id_fk)),'original': 'images/products/2018/08/carousel1.jpg'})
#seeder.add_entity(partner_stock,cantidad,{'product':lambda x: Product.objects.get(pk=random.randint(1,id_fk)),"price_currency": "DOLLAR",'partner': lambda x: partner_class.objects.get(pk=random.randint(1,id_fk)),"num_in_stock": random.randint(0,30)})

#seeder.add_entity(User,cantidad,{'is_staff':random.randint(0,1),'is_active':True,"password": 'a1234567890'})

#pk = seeder.execute()

#acortar_nombres()
#cambiar_contrasenas()