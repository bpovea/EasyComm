from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

# from oscar.core.loading import get_class
from . import views


# AboutUsView = get_class('help.views', 'AboutUsView')
# ContactUsView = get_class('help.views', 'ContactUsView')
# TermsView = get_class('help.views', 'TermsView')


urlpatterns = [
    url(r'^faq/', views.FaqView.as_view(), name='faq'),

    #API
	url(r'^api/faqs/$', csrf_exempt(views.faqList)),
	url(r'^api/faqs/(?P<pk>[0-9]+)$', csrf_exempt(views.faqDetail))
]
