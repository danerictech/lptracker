__author__ = 'daneel'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^index$', views.IndexView.as_view(), name='index'),
    url(r'^transits/$', views.TransitsView.as_view(), name='transits'),
    url(r'^addTransit/$', views.addTransit, name='transit'),
]