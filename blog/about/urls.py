from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
  url(r'^$', views.main, name='about'),
  url(r'^thankyou/$', views.thankyou, name='thankyou'),
]

# from django.conf import settings