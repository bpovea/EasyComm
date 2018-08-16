from django_seed import Seed
from django.conf import settings
import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EasyComm.settings')
import django
django.setup()
seeder = Seed.seeder()

from EasyComm_apps.help import models


seeder.add_entity(models.Faq, 5)

inserted_pks = seeder.execute()