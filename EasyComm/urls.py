from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from . import views
from EasyCommAPI.apps import application as api
from oscar.app import application as oscar

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^admin/', admin.site.urls),

    #url(r'', application.urls),
    url(r'^api/', api.urls),
    url(r'', oscar.urls),

    url(r'home/',views.home,name = "home"),
    url(r'about_us/',views.about_us,name = "about_us"),
    url(r'contact_us/',views.contact_us,name = "contact_us"),
    url(r'partners/',views.partners,name = "partners"),
    url(r'categories/',views.categories,name = "categories"),
    

    #  URL Byron
    #  Help -> Faqs
    url(r'^help/', include(('EasyComm_apps.help.urls','help'), namespace="help")),
]




