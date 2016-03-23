from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index_five, name='index_five'),
    url(r'^index/$', views.index_five, name='index_five'),
    url(r'^index_all/$', views.index_all, name='index_all'),
    url(r'^category/(?P<slug>[\w-]+)', views.category, name='category'),
    url(r'^(?P<slug>[\w-]+)/', views.detail, name='detail'),
]