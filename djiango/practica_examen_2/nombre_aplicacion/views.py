from django.shortcuts import render, get_object_or_404
from .models import Post

def principal(request):
    posts = Post.objects.all()
    return render(request, 'nombre_app/principal.html', {'posts': posts})

def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'nombre_app/detalle_post.html', {'post': post})