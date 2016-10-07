from django.conf.urls import include, url
from django.contrib import admin
from bailout.views import index, data, links, member_search, financial_services_committee

urlpatterns = [
    url(r'^$', index),
    url(r'^data$', data),
    url(r'^links$', links),
    url(r'^member_search$', member_search),
    url(r'^financial_services_committee$', financial_services_committee)

]