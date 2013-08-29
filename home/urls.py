from django.conf.urls import patterns, url
from home import views

urlpatterns = patterns('',
    url(r'^$', views.main),
    url(r'^getItems$', views.getItems),
    url(r'^computeSummary$', views.computeSummary),
)