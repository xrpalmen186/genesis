from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import IngredienteForm
from .models import Ingrediente, CategoriaIngrediente
from django.views.decorators.http import require_http_methods

def ingrediente_crear(request):
    """
    Vista para crear un ingrediente (función corregida).
    Elimina UnboundLocalError asegurando que 'form' se define en ambas ramas.
    """
    if request.method == 'POST':
        form = IngredienteForm(request.POST)
        if form.is_valid():
            ingrediente = form.save()
            messages.success(request, 'Ingrediente creado correctamente.')
            # redirige al detalle (cambiar a 'app:ingredientes_list' si prefieres lista)
            return redirect('app:ingrediente_detalle', pk=ingrediente.pk)
        # si no es válido, caemos abajo y re-renderizamos con errores (form queda definido)
    else:
        # rama GET: siempre definir form antes de renderizar
        form = IngredienteForm()

    return render(request, 'app/ingredientes_crear.html', {'form': form})


def ingrediente_detalle(request, pk):
    ingrediente = get_object_or_404(Ingrediente, pk=pk)
    return render(request, 'app/ingredientes_detalle.html', {'ingrediente': ingrediente})


def ingrediente_editar(request, pk):
    ingrediente = get_object_or_404(Ingrediente, pk=pk)

    if request.method == 'POST':
        form = IngredienteForm(request.POST, instance=ingrediente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ingrediente actualizado correctamente.')
            return redirect('app:ingrediente_detalle', pk=ingrediente.pk)
        # si no es válido, se re-renderiza mostrando errores
    else:
        form = IngredienteForm(instance=ingrediente)

    return render(request, 'app/ingredientes_editar.html', {
        'form': form,
        'ingrediente': ingrediente,
    })


@require_http_methods(["GET", "POST"])
def ingrediente_borrar(request, pk):
    """
    GET  -> muestra pantalla de confirmación
    POST -> borra el ingrediente y redirige a la lista con un message
    """
    ingrediente = get_object_or_404(Ingrediente, pk=pk)

    if request.method == 'POST':
        nombre = str(ingrediente)
        ingrediente.delete()
        messages.success(request, f'Ingrediente "{nombre}" eliminado correctamente.')
        return redirect('app:ingredientes_list')

    # GET: mostrar confirmación
    return render(request, 'app/ingredientes_borrar.html', {
        'ingrediente': ingrediente
    })

# Create your views here.
def inicio(request):
    return render(request, 'app/inicio.html')

def ingredientes_lista(request):
    ingredientes = Ingrediente.objects.all()
    categorias = CategoriaIngrediente.objects.all()

    categoria_filtro = request.GET.get('categoria')
    refrigerado_filtro = request.GET.get('refrigerado')
    nombre_filtro = request.GET.get('nombre')

    if categoria_filtro:
        ingredientes = ingredientes.filter(categoria=categoria_filtro)
    if refrigerado_filtro:
        ingredientes = ingredientes.filter(refrigerado=True)
    if nombre_filtro:
        ingredientes = ingredientes.filter(nombre__icontains=nombre_filtro)


    return render(request, 'app/ingredientes_lista.html', {'categorias':categorias, 'ingredientes':ingredientes})