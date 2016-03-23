from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .forms import EmailForm
from django.views.generic import TemplateView


def main(request):
  form = EmailForm(request.POST or None)
  if request.method == 'POST':
    if form.is_valid():
      subject = form.cleaned_data['name']
      from_email = form.cleaned_data['email']
      message = form.cleaned_data['message']
      botcheck = form.cleaned_data['botcheck']
      if botcheck.upper() == 'NOTABOT':
        try:
          send_mail(subject, message, from_email, ['admin@jamesmieding.com'])
          return HttpResponseRedirect('/about/thankyou/')
        except:
          return HttpResponseRedirect('/about/')
      else:
        botfailure = "If you aren't a bot, type the phrase in the field."
        return render(request, 'about/base_about.html', {'form':form, 'botfailure':botfailure})
  return render(request, 'about/base_about.html', {'form':form})

def thankyou(request):
  return render(request, 'about/thankyou.html')


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
