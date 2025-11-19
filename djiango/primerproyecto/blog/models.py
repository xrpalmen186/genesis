from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    edad = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.nombre}, {self.apellido}"
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        
    
    
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    # autor = models.CharField(max_length=60)
    # cargarme la base de datospara hacer esto (IDEA: crear pagina donde se muestren todos los posts de un autor)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=True) # si autor lo hubieramos creado debajo Autor iría con ''
    cuerpo = models.TextField()
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"({self.id}) {self.titulo}"
