from django.urls import path
from . import views

app_name = 'app'


urlpatterns = [
    path('', views.inicio, name='inicio'),
    
    path('relaciones', views.relaciones, name='relaciones'),
    
    path('recetas', views.recetas_lista, name='recetas_lista'),
    path('receta/<int:pk>', views.receta_detalle, name='receta_detalle'),
    path('receta/<int:receta_pk>/agregar_ingrediente/<int:ingrediente_pk>', views.receta_agregar_ingrediente, name='receta_agregar_ingrediente'),
    path('receta/<int:receta_pk>/eliminar_ingrediente/<int:ingrediente_pk>', views.receta_eliminar_ingrediente, name='receta_eliminar_ingrediente'),
    
    path('ingredientes', views.IngredientesListaView.as_view(), name='ingredientes_lista'),
    path('ingredientes/crear', views.IngredientesNuevoView.as_view(), name='ingrediente_crear'),
    path('ingrediente_detalle/<int:pk>', views.ingrediente_detalle, name='ingrediente_detalle'),
    path('ingrediente_editar/<int:pk>', views.IngredientesEditarView.as_view(), name='ingrediente_editar'),
    path('ingredientes/<int:pk>/borrar/', views.IngredientesEliminarView.as_view(), name='ingrediente_borrar'),
]