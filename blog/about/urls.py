from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
  url(r'^$', views.temp, name='about')
    # url(r'^send/$', sendmail),
    # url(r'^thankyou/$', TemplateView.as_view(template_name='thankyou.html'), name='thankyou'),
    # url(r'^$', TemplateView.as_view(template_name='about.html'), name='about'),
]

# from django.conf import settings