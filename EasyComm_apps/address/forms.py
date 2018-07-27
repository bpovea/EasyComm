from django import forms
from django.utils.translation import ugettext_lazy as _

from oscar.apps.address import forms as address_forms
from oscar.core.loading import get_model

# Models
Country = get_model('address','Country')
UserAddress = get_model('address', 'UserAddress')


class UserAddressForm(address_forms.UserAddressForm):
    line1 = forms.CharField(
        label=_('Dirección'),
        max_length=255)

    country = forms.ModelChoiceField(
        label=_('País'),
        queryset=Country.objects.filter(is_shipping_country=True),
        initial='EC')

    #identity_to_invoice = forms.CharField(
    #    label=_('Cedula/RUC'),
    #    max_length=13)

    #identity_type = forms.ModelChoiceField(
    #    label=_('Tipo de identificación'),
    #    queryset=IDENTIFICATION_CHOICES)

    class Meta:
        fields = (
            'title', 'first_name', 'last_name',
            'country', 'province', 'city',
            'line1', 'phone_number', 'notes'
        )
        model = UserAddress

    def __init__(self, user, *args, **kwargs):
        super(UserAddressForm, self).__init__(user, *args, **kwargs)
        self.instance.user = user
        self.fields['province'].required = True
        self.fields['city'].required = True
        #self.fields['postcode'].required = False
        #self.fields['identity_to_invoice'].required = True
        #self.fields['identity_type'].required = True