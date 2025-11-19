from django.shortcuts import render
from .models import Ingrediente

# Create your views here.
def inicio(request):
    return render(request, 'app/inicio.html')

def ingredientes_list(request):
    ingredientes = Ingrediente.objects.all()
    
    categorias = Ingrediente.objects.values_list('categoria', flat=True).distinct()
    categorias_ingredientes = {categoria: Ingrediente.objects.filter(categoria=categoria) for categoria in categorias}
    return render(request, 'app/ingredientes_list.html', {'ingredientes': ingredientes})