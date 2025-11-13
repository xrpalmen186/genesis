from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('post/<int:pk>', views.detalle_post, name='detalle_post'),
    
    #todos los posts del autor
    path('autor/<int:pk>', views.autor_posts, name='autor_posts'), #1. URL creada (parametro "pk") (2. view "autor_posts" (3. template "autor_posts.html"))
    
    #pagina con todos los autores
    path('autores', views.autores, name='autores'),
    
    #formulario para añadir autores
    path('autor/nuevo', views.nuevo_autor, name='nuevo_autor'),
    
    #formulario para editar un autor especifico
    path('autor/editar/<int:pk>', views.editar_autor, name='editar_autor'),
    
    #eliminar autor
    path('autor/eliminar/<int:pk>', views.eliminar_autor, name='eliminar_autor'),
    
    #detalle autor
    path('autor/detalle/<int:pk>', views.detalle_autor, name='detalle_autor'),
]