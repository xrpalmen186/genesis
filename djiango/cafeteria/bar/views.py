from django.shortcuts import render, get_object_or_404
from .models import Carta

# Create your views here.
def bar(request):
    productos = Carta.objects.all()
    return render(request, 'bar/bar.html', {'productos': productos})

def detalle_producto(request, pk):
    producto = get_object_or_404(Carta, pk=pk)
    return render(request, 'bar/detalle_producto.html', {'producto': producto})