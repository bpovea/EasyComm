from django.contrib import admin
from oscar.core.loading import get_model
from oscar.apps.address.admin import *

City = get_model('address', 'City')
Province = get_model('address', 'Province')

admin.site.register(City)
admin.site.register(Province)

