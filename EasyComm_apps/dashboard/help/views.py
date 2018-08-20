from django.views import generic

from oscar.core.loading import get_classes, get_model

from EasyComm_apps.help.models import Faq

class FaqListView(generic.ListView):
    model = Faq
    template_name = "dashboard/help/faq_list.html"
    context_object_name = "faqs"
    