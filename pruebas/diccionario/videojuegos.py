

videojuegos = []
numVideojuegos = int(input("Número de videojuegos: "))

for i in range(numVideojuegos):
    videojuego = {}
    
    videojuego["nombre"] = input("Nombre: ")
    videojuego["valoración"] = int(input("Valoración: "))
    videojuego["categoría"] = input("Categoría: ")
    
    videojuegos.append(videojuego)
    
print(videojuegos)

#mostrar una lista con todos los nombres

# calculamos la media de todas las valoraciones

media = 0

for videojuego in videojuegos:
    print(videojuego["nombre"])
    media += videojuego["valoración"]
    
media = media / len(videojuegos)
print(f"La media de todas las valoraciones es: {media}")


# TODO: Para mañana
'''
Usando list compresion haremos una lista con todos los nombres y otra lista con todas las valoraciones. (En una sola linea creamos cada lista)
'''

nombres = [videojuego["nombre"] for videojuego in videojuegos]
valoraciones = [videojuego["valoración"] for videojuego in videojuegos]
