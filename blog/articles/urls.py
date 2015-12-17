from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^index/$', views.index_five, name='index_five'),
    url(r'^index_all/$', views.index_all, name='index_all'),
    url(r'^(?P<slug>[\w-]+)/', views.detail, name='detail')
]