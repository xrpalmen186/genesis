from django.shortcuts import render
from .models import Ingrediente, CategoriaIngrediente
from .forms import FiltroIngredientesForm

# Create your views here.
def inicio(request):
    return render(request, 'app/inicio.html')

def ingredientes_list(request):
    ingredientes = Ingrediente.objects.all()
    categorias = CategoriaIngrediente.objects.all()
    
    categoria_filtro = request.GET.get('categoria')
    nombre_filtro = request.GET.get('nombre')
    cantidad_filtro = request.GET.get('cantidad')
    unidades_filtro = request.GET.get('unidades')
    
    if categoria_filtro:
        ingredientes = ingredientes.filter(categoria__categoria=categoria_filtro)
    if nombre_filtro:
        ingredientes = ingredientes.filter(nombre__startswith=nombre_filtro) | ingredientes.filter(nombre__icontains=nombre_filtro)
    if cantidad_filtro:
        ingredientes = ingredientes.filter(cantidad=cantidad_filtro)
    if unidades_filtro:
        ingredientes = ingredientes.filter(unidad=unidades_filtro)
        
    formulario_filtro = FiltroIngredientesForm(request.GET)
    if formulario_filtro.is_valid():
        categoria_filtro = formulario_filtro.cleaned_data['categoria']
        nombre_filtro = formulario_filtro.cleaned_data['nombre']
        cantidad_filtro = formulario_filtro.cleaned_data['cantidad']
        unidades_filtro = formulario_filtro.cleaned_data['unidades']
        
        if categoria_filtro:
            ingredientes = ingredientes.filter(categoria__categoria=categoria_filtro)
        if nombre_filtro:
            ingredientes = ingredientes.filter(nombre__startswith=nombre_filtro) | ingredientes.filter(nombre__icontains=nombre_filtro)
        if cantidad_filtro:
            ingredientes = ingredientes.filter(cantidad=cantidad_filtro)
        if unidades_filtro:
            ingredientes = ingredientes.filter(unidad=unidades_filtro)
        
    return render(request, 'app/ingredientes_list.html', {'categorias': categorias, 'ingredientes': ingredientes, 'formulario_filtro': formulario_filtro})


# TAREA MARTES: (en el movil)