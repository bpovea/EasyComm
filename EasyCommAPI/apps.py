from oscarapi.app import RESTApiApplication
from django.conf.urls import url
from . import views

class MyRESTApiApplication(RESTApiApplication):

    def get_urls(self):
        urls = [
        	url(r'^$', views.api_root, name='api-root'),
        	url(r'^products/$',views.ProductList.as_view(), name='product-list'),
        	url(r'^products-categories/$',views.products_categories.as_view(), name='products-category-list'),
        	url(r'^products-categories/(?P<pk>[0-9]+)/$',views.category_details.as_view(), name='products-category-details'),
        	url(r'^products-class/$',views.products_class.as_view(), name='products-class-list'),

            url(r'^profile/(?P<pk>[0-9]+)/$',views.profile_details.as_view(), name='profile-details'),

        	url(r'^report-products/$',views.report_products.as_view(), name='report-products'),
            url(r'^report-orders/$',views.report_orders.as_view(), name='report-orders'),
            url(r'^report-baskets-open/$',views.report_baskets_open.as_view(), name='report-baskets-open'),
        ]

        return urls + super(MyRESTApiApplication, self).get_urls()

application = MyRESTApiApplication()



