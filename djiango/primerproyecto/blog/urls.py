from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('post/<int:pk>', views.detalle_post, name='detalle_post'),
    
    #todos los posts del autor
    path('autor/<int:pk>', views.autor_posts, name='autor_posts'), #1. URL creada (parametro "pk") (2. view "autor_posts" (3. template "autor_posts.html"))
    
    #pagina con todos los autores
    path('autores', views.autores, name='autores'),
]