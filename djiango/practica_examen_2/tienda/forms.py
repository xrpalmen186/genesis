from django import forms
from django.forms import inlineformset_factory
from .models import Producto, Pedido, LineaPedido

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'categoria', 'info_nutricional']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'info_nutricional': forms.Select(attrs={'class': 'form-select'}),
        }

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente']
        widgets = {
            'cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del cliente'}),
        }

# FORMSET: Esto es magia para los exámenes. 
# Crea un conjunto de formularios de LineaPedido vinculados a un Pedido automáticamente.
LineaPedidoFormSet = inlineformset_factory(
    Pedido,             # Modelo Padre
    LineaPedido,        # Modelo Hijo
    fields=['producto', 'cantidad'], # Campos a editar
    extra=3,            # Cuántas filas vacías mostrar
    can_delete=True,    # Permitir borrar líneas
    widgets={
        'producto': forms.Select(attrs={'class': 'form-select'}),
        'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
    }
)