from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def home(request):
  most_recent_post = Post.objects.latest('published_date')
  return render(request, "articles/home.html", {'most_recent_post': most_recent_post})

def index_five(request):
  posts = Post.objects.order_by('published_date').reverse()[:5]
  return render(request, "articles/index.html", {'posts': posts})

def index_all(request):
  posts = Post.objects.order_by('published_date').reverse()
  return render(request, "articles/index.html", {'posts': posts})

def detail(request, slug):
  post = get_object_or_404(Post, slug=slug)
  return render(request, "articles/detail.html", {'post': post})

def resources(request):
  return render(request, "resources.html")