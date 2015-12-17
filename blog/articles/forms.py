from django import forms
from django.utils.text import slugify

from .models import Post

# class PostForm(forms.ModelForm):
# 	class Meta:
# 		model = Post
# 		fields = [
# 			'title',
# 			'text',
# 			'published_date',
# 			'categories'
# 		]

# 	def save(self):
# 		instance = super(AddForm, self).save(commit=False)
# 		instance.slug = slugify(instance.title)
# 		instance.save()

# 		return instance

# class ModelNameForm(forms.ModelForm):
# 	class Meta:
# 		model = SignUp
# 		fields = ['email']
	# def clean_email(self):
	# 	email = self.cleaned_data.get('email')
	# 	email_base, provider = email.split('@')
	# 	domain, extension = provider.split('.')
	# 	if not "edu" in email:
	# 		raise forms.ValidationError("please use valid email")
	# 	return email

	# def clean_full_name(self):
	# 	full_name = self.cleaned_data.get('full_name')
	# 	Validation code goes here.
	# 	return full_name