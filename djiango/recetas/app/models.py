from django.db import models

# Create your models here.

# class CategoriaChoices(models.TextChoices):
#     LEGUMBRES = "LE", "Legumbres"
class CategoriaIngrediente(models.Model):
    categoria = models.CharField(max_length=50)
    
    def __str__(self):
        return self.categoria

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    # categoria = models.CharField(max_length=50, choices=CategoriaChoices)
    categoria = models.ForeignKey(CategoriaIngrediente, on_delete=models.CASCADE)
    cantidad = models.CharField(max_length=50)
    unidad = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre