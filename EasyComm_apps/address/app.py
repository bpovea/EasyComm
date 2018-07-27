from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from oscar.core.application import Application
from . import views

class AddressApplication(Application):
    name = 'address'

    def get_urls(self):
        urls = [
            url(r'^cities/$',
                login_required(views.city_list),
                name='city-list'),
        ]
        return self.post_process_urls(urls)


application = AddressApplication()