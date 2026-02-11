from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    # путь начинается с папки templates
    return render(request, 'post/post_list.html', {'posts': posts})

def post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post/post_details.html', {'post': post})

