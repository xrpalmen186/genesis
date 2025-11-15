from django.shortcuts import render, get_object_or_404
from .models import Post

def principal(request):
    context = Post.objects.all()
    return render(request, 'wiki/index.html', {'posts': context})

def detalle_post(request, pk):
    context = get_object_or_404(Post, pk=pk)
    return render(request, 'wiki/detalle_post.html', {'post': context})