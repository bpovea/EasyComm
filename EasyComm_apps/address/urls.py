from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^cities/', views.city_list, name='city-list'),
]
