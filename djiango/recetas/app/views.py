from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import *
from .models import Ingrediente, CategoriaIngrediente, Receta
from django.views.decorators.http import require_http_methods
from django.forms import formset_factory

# def ingrediente_crear(request):
#     """
#     Vista para crear un ingrediente (función corregida).
#     Elimina UnboundLocalError asegurando que 'form' se define en ambas ramas.
#     """
#     if request.method == 'POST':
#         form = IngredienteForm(request.POST)
#         if form.is_valid():
#             ingrediente = form.save()
#             messages.success(request, 'Ingrediente creado correctamente.')
#             # redirige al detalle (cambiar a 'app:ingredientes_list' si prefieres lista)
#             return redirect('app:ingrediente_detalle', pk=ingrediente.pk)
#         # si no es válido, caemos abajo y re-renderizamos con errores (form queda definido)
#     else:
#         # rama GET: siempre definir form antes de renderizar
#         form = IngredienteForm()

#     return render(request, 'app/ingredientes_crear.html', {'form': form})


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


def ingrediente_crear(request):
    
    formularios = formset_factory(IngredientesForm, extra=3)
    
    if request.method == "POST":
        formset = formularios(request.POST)
        
        if formset.is_valid():
            for form in formset:
                if form.is_valid():
                    form.save() #Usando modelform todo es más facil
                return redirect('app:ingredientes_lista')
        else:
            print(formset.errors)
    else:
        formset = formularios()
    
    return render(request, 'app/ingredientes_crear.html', {'formularios': formset})

def relaciones(request):
    recetas = Receta.objects.all()
    ingredientes = Ingrediente.objects.all()
    form = formset_factory(RecetaIngredientesForm, extra=3)
    
    if request.method == "POST":
        formset = form(request.POST)
        
        if formset.is_valid():
            for form in formset:
                if form.is_valid():
                    form.save()
                return redirect('app:relaciones')
        else:
            print(formset.errors)
    else:
        formset = form()
    
    return render(request, 'app/relaciones.html', {'recetas': recetas, 'ingredientes': ingredientes, 'formularios': formset})


def recetas_lista(request):
    recetas = Receta.objects.all()
    return render(request, 'app/recetas_lista.html', {'recetas': recetas})


def receta_detalle(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    ingredientes = Ingrediente.objects.all()
    return render(request, 'app/receta_detalle.html', {'receta': receta, 'ingredientes': ingredientes})

def receta_agregar_ingrediente(request, receta_pk, ingrediente_pk):
    receta = get_object_or_404(Receta, pk=receta_pk)
    ingrediente = get_object_or_404(Ingrediente, pk=ingrediente_pk)
    
    receta.ingredientes.add(ingrediente)
    
    return redirect('app:receta_detalle', pk=receta.pk)

def receta_eliminar_ingrediente(request, receta_pk, ingrediente_pk):
    receta = get_object_or_404(Receta, pk=receta_pk)
    ingrediente = get_object_or_404(Ingrediente, pk=ingrediente_pk)
    
    receta.ingredientes.remove(ingrediente)
    
    return redirect('app:receta_detalle', pk=receta.pk)