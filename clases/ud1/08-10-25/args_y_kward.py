def sumar(n, *args):
    total = n
    for x in args:
        total += x
    print(total)

def comidas(titulo="gazpacho", **kwargs):
    print(f"Receta de {titulo}")
    print("Más info sobre la receta (ingredientes, preparación...):")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
        
sumar(3, 4, 5, 6, 7)
comidas(titulo="gazpacho", ingredientes="tomate, pan, aceite, ajo, pepino", preparacion="cocinar...")