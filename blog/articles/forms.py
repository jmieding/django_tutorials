from django import forms

class CommentForm(forms.Form):
  text = forms.CharField(widget=forms.Textarea(attrs={'cols':90, 'rows':3, 'placeholder':'Leave a comment...', 'required':True}))