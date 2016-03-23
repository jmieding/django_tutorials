from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
  password_again = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'required':True, 'size':20}))
  class Meta:
    model = User
    fields = [ 'username', 'password', 'email']
  