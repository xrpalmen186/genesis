from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('productos/', views.ProductoListView.as_view(), name='lista_productos'),
    path('productos/crear/', views.ProductoCreateView.as_view(), name='crear_producto'),
    path('pedidos/crear/', views.crear_pedido_con_detalles, name='crear_pedido'),
]