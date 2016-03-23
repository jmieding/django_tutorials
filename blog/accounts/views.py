from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserForm
from django.contrib.auth.models import User

# Create your views here.

def register(request):
  # if request.user.is_authenticated() == True:
    # You are already logged in!
    # return HttpResponseRedirect('/')
  form = UserForm(request.POST or None)
  if request.method == 'POST':
    if form.is_valid():
      username = form.cleaned_data['username']
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']
      password_check = form.cleaned_data['password_again']
      if password == password_check:
        user = User.objects.create_user(username, email, password)
        user.save()
      return HttpResponseRedirect('articles/' + next)
      # redirect to login, or automatically login
  return render(request, 'accounts/register.html', {'form':form})