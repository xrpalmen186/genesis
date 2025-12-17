from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Producto, Pedido
from .forms import ProductoForm, PedidoForm, LineaPedidoFormSet

# --- VISTAS BASADAS EN CLASES (CBV) ---
# Ideales para CRUDs sencillos (Listar, Crear uno simple)

class ProductoListView(ListView):
    model = Producto
    template_name = 'tienda/lista_productos.html'
    context_object_name = 'productos'

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'tienda/crear_producto.html'
    success_url = reverse_lazy('tienda:lista_productos')


# --- VISTA BASADA EN FUNCIÓN (FBV) ---
# Ideal para lógica compleja como guardar un Pedido y sus Líneas a la vez (Master-Detail)

def crear_pedido_con_detalles(request):
    if request.method == 'POST':
        form_pedido = PedidoForm(request.POST)
        # Pasamos request.POST al formset también
        formset_lineas = LineaPedidoFormSet(request.POST)
        
        if form_pedido.is_valid() and formset_lineas.is_valid():
            # 1. Guardamos el pedido (Padre)
            pedido = form_pedido.save()
            
            # 2. Asociamos el formset al pedido recién creado y guardamos
            formset_lineas.instance = pedido
            formset_lineas.save()
            
            return redirect('tienda:lista_productos') # O a donde quieras ir
            
    else:
        form_pedido = PedidoForm()
        formset_lineas = LineaPedidoFormSet()
    
    context = {
        'form_pedido': form_pedido,
        'formset_lineas': formset_lineas
    }
    return render(request, 'tienda/crear_pedido.html', context)