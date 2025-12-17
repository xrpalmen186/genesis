from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class InfoNutricional(models.Model):
    # Relación 1 a 1: Un producto tiene una sola ficha nutricional y viceversa
    calorias = models.PositiveIntegerField()
    es_vegano = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Info: {self.calorias} kcal"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    # Relación 1 a N: related_name permite acceder desde categoria.productos.all()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    # Relación 1 a 1
    info_nutricional = models.OneToOneField(InfoNutricional, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} ({self.precio}€)"

class Pedido(models.Model):
    cliente = models.CharField(max_length=100) # Simplificado para el examen
    fecha = models.DateTimeField(auto_now_add=True)
    # Relación N a M con tabla intermedia
    productos = models.ManyToManyField(Producto, through='LineaPedido', related_name='pedidos')

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente}"

class LineaPedido(models.Model):
    # La tabla intermedia (through)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    
    # Truco examen: Guardar el precio al momento de la compra por si el producto sube de precio mañana
    precio_unitario = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Sobreescribimos save para autoguardar el precio si no viene dado
        if not self.precio_unitario:
            self.precio_unitario = self.producto.precio
        super().save(*args, **kwargs)