from django_seed import Seed
from django.conf import settings
import os
import sys
import django
from oscar.core.loading import get_class, get_model
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EasyComm.settings')
django.setup()

from EasyComm_apps.help import models

Product = get_model('catalogue', 'product')
product_class = get_model('catalogue', 'ProductClass')
category_class = get_model('catalogue', 'Category')
partner_class = get_model('partner', 'Partner')
partner_adress = get_model('partner','PartnerAddress')
country_class = get_model('address', 'Country')
product_category_class = get_model('catalogue', 'ProductCategory')
product_image = get_model('catalogue', 'ProductImage')
partner_stock = get_model('partner', 'StockRecord')

seeder = Seed.seeder()


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

seeder.execute()

