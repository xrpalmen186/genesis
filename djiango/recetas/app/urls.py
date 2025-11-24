from django.urls import path
from . import views

app_name = 'app'


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('ingredientes', views.ingredientes_lista, name='ingredientes_lista'),
    path('ingredientes/crear', views.ingrediente_crear, name='ingrediente_crear'),
    path('ingrediente_detalle/<int:pk>', views.ingrediente_detalle, name='ingrediente_detalle'),
    path('ingrediente_editar/<int:pk>', views.ingrediente_editar, name='ingrediente_editar'),
    path('ingredientes/<int:pk>/borrar/', views.ingrediente_borrar, name='ingrediente_borrar'),
]