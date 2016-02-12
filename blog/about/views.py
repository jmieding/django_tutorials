from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .models import EmailForm
from django.views.generic import TemplateView


def temp(request):
  return render(request, 'about/base_about.html')

# def sendmail(request):
#   if request.method == 'POST':
#     form = EmailForm(request.POST)
#     if form.is_valid():
#       firstname = form.cleaned_data['firstname']
#       lastname = form.cleaned_data['lastname']
#       email = form.cleaned_data['email']
#       subject = form.cleaned_data['subject']
#       botcheck = form.cleaned_data['botcheck'].lower()
#       message = form.cleaned_data['message']
#       if botcheck == 'yes':
#         try:
#           fullemail = firstname + " " + lastname + " " + "<" + email + ">"
#           send_mail(subject, message, fullemail, ['SENDTOUSER@DOMAIN.COM'])
#           return HttpResponseRedirect('/about/thankyou/')
#         except:
#           return HttpResponseRedirect('/about/')
#     else:
#       return HttpResponseRedirect('/about/')
#   else:
#     return HttpResponseRedirect('/about/')  
