from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Autor #desde la app en la que está importamos ... (de ahí el .)
from .forms import AutorFormulario, AutorModelFormulario

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

#vista para mostrar formulario de añadir autores
def nuevo_autor (request):
    if request.method == 'POST':
        form = AutorModelFormulario(request.POST)
        if form.is_valid():
            #almacenar en la base de datos (si no usamos model form)
            
            # nombre = form.cleaned_data['nombre']
            # apellido = form.cleaned_data['apellido']
            # edad = form.cleaned_data['edad']
            # email = form.cleaned_data['email']
            
            # Autor.objects.create(
            #     nombre=nombre,
            #     apellido=apellido,
            #     edad=edad,
            #     email=email
            # )
            
            form.save() #si usamos el model form
            return redirect('autores')
    else:
        form = AutorModelFormulario()
        contexto = {'form': form, 'estado': 'add'}
    
    return render(request, 'blog/autor_crud.html', contexto)

#vista para mostrar formulario de edición de un autor
def editar_autor (request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorModelFormulario(request.POST, instance=autor) #crea una instancia con sus datos
        if form.is_valid():
            form.save()
            return redirect('autores')
    else:
        form = AutorModelFormulario(instance=autor)
        contexto = {'form': form, 'estado': 'edit'}
    
    return render(request, 'blog/autor_crud.html', contexto)

#vista para eliminar autor pide confirmacion en eliminar_autor
def eliminar_autor (request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('autores')
    return render(request, 'blog/eliminar_autor.html', {'autor': autor})

#vista para mostrar detalles del autor
def detalle_autor (request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    
    #en el caso de que sea GET coge 
    if request.method == 'GET':
        form = AutorModelFormulario(instance=autor)
        contexto = {'form': form, 'estado': 'detail'}
        return render(request, 'blog/autor_crud.html', contexto)
    else:
        return redirect('autores')
        