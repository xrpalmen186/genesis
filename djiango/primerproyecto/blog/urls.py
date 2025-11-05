from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('post/<int:pk>', views.detalle_post, name='detalle_post'),
]