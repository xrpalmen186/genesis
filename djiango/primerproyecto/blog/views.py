from django.shortcuts import get_object_or_404, render
from .models import Post, Autor #desde la app en la que está importamos ...

# Create your views here.
def inicio (request):
    autores = Autor.objects.all() #autores
    entradas = Post.objects.all() #data set
    contexto = {'entradas': entradas, 'autores': autores}
    return render(request, 'blog/inicio.html', contexto)

def detalle_post (request, pk):
    entrada = get_object_or_404(Post, pk=pk)
    contexto = {'post': entrada}
    return render(request, 'blog/detalle_post.html', contexto)

def autor_posts (request, pk): #4. creamos la vista
    autor = get_object_or_404(Autor, pk=pk) #AUTORES
    entradas = Post.objects.filter(autor=autor) #PUBLICACIONES
    contexto = {'posts': entradas, 'autor': autor} #le pasamos las publicaciones y los autores
    return render(request, 'blog/autor_posts.html', contexto)

#vista para mostrar todos los autores
def autores (request):
    autores = Autor.objects.all()
    contexto = {'autores': autores}
    return render(request, 'blog/autores.html', contexto)