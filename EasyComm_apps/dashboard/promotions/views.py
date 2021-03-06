from oscar.apps.dashboard.promotions.views import *
from EasyComm_apps.promotions.conf import PROMOTION_CLASSES
from EasyComm_apps.promotions.models import Faq
from oscar.core.loading import get_class

from .forms import PromotionTypeSelectForm as SelectForm

class ListView(generic.TemplateView):
    template_name = 'dashboard/promotions/promotion_list.html'

    def get_context_data(self):
        # Need to load all promotions of all types and chain them together
        # no pagination required for now.
        data = []
        num_promotions = 0
        for klass in PROMOTION_CLASSES:
            objects = klass.objects.all()
            num_promotions += objects.count()
            data.append(objects)
        promotions = itertools.chain(*data)
        ctx = {
            'num_promotions': num_promotions,
            'promotions': promotions,
            'select_form': SelectForm(),
        }
        return ctx

class CreateRedirectView(generic.RedirectView):
    permanent = True

    def get_redirect_url(self, **kwargs):
        code = self.request.GET.get('promotion_type', None)
        urls = {}
        for klass in PROMOTION_CLASSES:
            urls[klass.classname()] = reverse('dashboard:promotion-create-%s' %
                                              klass.classname())
        return urls.get(code, None)

class CreateFaqView(CreateView):
    model = Faq
    fields = ['name','title','subTitle','description','link_url','button','image']

class UpdateFaqView(UpdateView):
    model = Faq
    fields = ['name','title','subTitle','description','link_url','button','image']

class DeleteFaqView(DeleteView):
    model = Faq