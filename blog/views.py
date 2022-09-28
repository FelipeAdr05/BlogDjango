from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def post(request, post_pk):
    posts = get_object_or_404(Post, pk=post_pk)
    return render(request, 'post.html', {'post': posts})