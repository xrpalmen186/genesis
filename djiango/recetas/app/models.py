from django.db import models

# Create your models here.

# class CategoriaChoices(models.TextChoices):
#     LEGUMBRE = "LE", "Legumbres"



class CategoriaIngrediente(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.nombre}"

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(CategoriaIngrediente, on_delete=models.CASCADE)
    refrigerado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.nombre} ({self.categoria})"

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ingredientes = models.ManyToManyField(Ingrediente, related_name='recetas', through='IngredienteReceta')
    
    def __str__(self) -> str:
        return f"{self.nombre}"

class IngredienteReceta(models.Model): # "Tiene" Relacion
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return f"{self.receta} - {self.ingrediente} - ({self.cantidad})"
    
    class Meta:
        unique_together = ('receta', 'ingrediente')

# Crear TextChoices y IntegerChoices (global)