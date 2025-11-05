from django.shortcuts import get_object_or_404, render
from .models import Post #desde la app en la que está importamos ...

# Create your views here.
def inicio (request):
    entradas = Post.objects.all() #data set
    contexto = {'entradas': entradas}
    return render(request, 'blog/inicio.html', contexto)

def detalle_post (request, pk):
    entrada = get_object_or_404(Post, pk=pk)
    contexto = {'post': entrada}
    return render(request, 'blog/detalle_post.html', contexto)