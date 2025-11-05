from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    
    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"


# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=60)
    # cargarme la base de datospara hacer esto (IDEA: crear pagina donde se muestren todos los posts de un autor)
    #autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    cuerpo = models.TextField()
    email = models.EmailField(null=True, blank=True)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"({self.id}) {self.titulo}"
