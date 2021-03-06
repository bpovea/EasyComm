from django import forms
from django.utils.translation import gettext_lazy as _

from oscar.core.loading import get_class
from oscar.forms.widgets import DatePickerInput

GeneratorRepository = get_class('dashboard.reports.utils',
                                'GeneratorRepository')


class ReportForm(forms.Form):
    generators = GeneratorRepository().get_report_generators()

    type_choices = []

    # para limitar los tipos de reportes a presentar
    code = ['user_analytics','submitted_baskets','vouchers']
    
    for generator in generators:
        if generator.code not in code:
            type_choices.append((generator.code, generator.description))
    report_type = forms.ChoiceField(widget=forms.Select(),
                                    choices=type_choices,
                                    label=_("Report Type"),
                                    help_text=_("Only the offer and order"
                                                " reports use the selected"
                                                " date range"))

    date_from = forms.DateField(label=_("Fecha inicio"), required=False,
                                widget=DatePickerInput)
    date_to = forms.DateField(label=_("Fecha fin"),
                              help_text=_("El reporte es inclusivo."),
                              required=False,
                              widget=DatePickerInput)
    download = forms.BooleanField(label=_("Descargar"), required=False)

    def clean(self):
        date_from = self.cleaned_data.get('Fecha inicio', None)
        date_to = self.cleaned_data.get('Fecha fin', None)
        if (all([date_from, date_to]) and self.cleaned_data['date_from'] >
                self.cleaned_data['date_to']):
            raise forms.ValidationError(_("Rango incorrecto de fecha."))
        return self.cleaned_data
