from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from .models import Post, Category, Comment

from django.contrib.auth.models import User
from .forms import CommentForm

# Create your views here.

def index_five(request):
  posts = Post.objects.filter(published=True).order_by('published_date').reverse()[:5]
  return render(request, "articles/index.html", {'posts': posts})

def index_all(request):
  posts = Post.objects.filter(published=True).order_by('published_date').reverse()
  return render(request, "articles/index.html", {'posts': posts})

def detail(request, slug):
  post = get_object_or_404(Post, slug=slug)
  form = CommentForm(request.POST or None)
  if request.method == 'POST' and request.user.is_authenticated():
    if form.is_valid():
      author = request.user
      text = form.cleaned_data['text']
      Comment.objects.create(author=author, text=text, post=post)
      return HttpResponseRedirect('articles/' + slug)
  return render(request, "articles/detail.html", {'post': post, 'form':form})

def resources(request):
  return render(request, "resources.html")

def category(request, slug):
  category = get_object_or_404(Category, slug=slug)
  posts = Post.objects.filter(categories=category, published=True).order_by('published_date').reverse()
  return render(request, "articles/index.html", {'posts': posts})