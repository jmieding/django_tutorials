from django import forms

class EmailForm(forms.Form):
  name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'required':True, 'size':30}))
  email = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'required':True, 'size':30}))
  message = forms.CharField(widget=forms.Textarea(attrs={'cols':70, 'rows':8, 'required':True}))
  botcheck = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'required':True, 'placeholder':'Type \'NOTABOT\''}))


  #   def save(self):
#     instance = super(AddForm, self).save(commit=False)
#     instance.slug = slugify(instance.title)
#     instance.save()

#     return instance

# class ModelNameForm(forms.ModelForm):
#   class Meta:
#     model = SignUp
#     fields = ['email']
  # def clean_email(self):
  #   email = self.cleaned_data.get('email')
  #   email_base, provider = email.split('@')
  #   domain, extension = provider.split('.')
  #   if not "edu" in email:
  #     raise forms.ValidationError("please use valid email")
  #   return email

  # def clean_full_name(self):
  #   full_name = self.cleaned_data.get('full_name')
  #   Validation code goes here.
  #   return full_name