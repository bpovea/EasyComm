from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import exceptions

from oscar.apps.address.abstract_models import AbstractUserAddress

class Province(models.Model):
    country = models.ForeignKey(
        'address.Country',
        on_delete=models.CASCADE,
        verbose_name=_("Country"),
        default='EC')
    iso_3166_2 = models.CharField(
        _('ISO 3166-2'), max_length=3, blank=True)
    name = models.CharField(
        _('Name'), max_length=30)

    @property
    def code(self):
        return self.country.code + '-' + self.iso_3166_2

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _('Provincia')
        verbose_name_plural = _('Provincias')


class City(models.Model):
    province = models.ForeignKey(
        'address.Province',
        on_delete=models.CASCADE,
        verbose_name=_("Province"))
    name = models.CharField(
        _('Name'), max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _('City')
        verbose_name_plural = _('Cities')


class UserAddress(AbstractUserAddress):
    province = models.ForeignKey(
        'address.Province',
        on_delete=models.CASCADE,
        verbose_name=_("Provincia"),
        blank=True,
        null=True)
    city = models.ForeignKey(
        'address.City',
        on_delete=models.CASCADE,
        verbose_name=_("Ciudad"),
        blank=True,
        null=True)

    def active_address_fields(self, include_salutation=True):
        """
        Return the non-empty components of the address, but merging the
        title, first_name and last_name into a single line.
        """
        fields = [self.line1, self.line2, self.line3,
                  self.line4, self.state, self.postcode]
        if include_salutation:
            fields = [self.salutation] + fields
        fields = [f.strip() for f in fields if f]
        try:
            fields.append(str(self.province)+' - '+str(self.city))
        except exceptions.ObjectDoesNotExist:
            pass
        return fields


from oscar.apps.address.models import *
