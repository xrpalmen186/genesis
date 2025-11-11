from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('post/<int:pk>', views.detalle_post, name='detalle_post'),
    #todos los posts del autor
    path('autor/<int:pk>', views.autor_posts, name='autor_posts'),
    #path('post/autor/<int:pk>', views.post_autor, name='post_autor'),
]