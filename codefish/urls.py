from django.conf.urls import patterns, url, include

from codefish.views import home

urlpatterns = patterns('',
    url(r'^$', 'codefish.views.home', name='home'),
)
