from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=60)
    cuerpo = models.TextField()
    email = models.EmailField(null=True, blank=True)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"({self.id}) {self.titulo}"