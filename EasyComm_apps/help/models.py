from django.db import models
from django.utils.translation import ugettext_lazy as _

class Faq(models.Model):
    question = models.CharField(_('Pregunta'),max_length=80)
    answer = models.TextField(_('Respuesta'),max_length=500,blank=True)
    image = models.ImageField(_('Imagen'),upload_to='employees',null=True,blank=True)
    STATUSES = [
    	(0, 'Desactivado'),
    	(1, 'Activo')
    ]
    status = models.PositiveSmallIntegerField(choices=STATUSES, default=1)