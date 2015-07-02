from django.conf.urls import patterns
from django.conf.urls import url

import views

urlpatterns = patterns('', 
    url(r'^$', views.show_equation_list),
)