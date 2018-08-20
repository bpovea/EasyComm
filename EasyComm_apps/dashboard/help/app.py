from django.conf.urls import url

from oscar.core.application import DashboardApplication
from oscar.core.loading import get_class


class HelpDashboardApplication(DashboardApplication):
    name = None
    default_permissions = ['is_staff']

    faq_list_view = get_class(
        'dashboard.help.views', 'FaqListView')

    def get_urls(self):
        urlpatterns = [
            url(r'^faqs/$', self.faq_list_view.as_view(),
                name='faq-list'),
        ]
        return self.post_process_urls(urlpatterns)


application = HelpDashboardApplication()
