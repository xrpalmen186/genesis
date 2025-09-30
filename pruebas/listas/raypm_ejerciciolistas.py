#!/usr/bin/env python3

'''
EJERCICIO PYTHON LISTAS - Raimundo Palma Méndez 2ºDAW
=====================================================

Una tienda de videojuegos quiere llevar un registro de las valoraciones que los clientes otorgan a sus productos.
Escribe un programa en Python que:

1. Disponga de una lista inicial con varios nombres de videojuegos (por ejemplo: ["Zelda", "FIFA", "Minecraft", "Call of Duty", "Animal Crossing"]).

2. Para cada videojuego de la lista, el programa debe preguntar al usuario una valoración entre 1 y 10 y almacenarla en otra lista paralela.

- Si el usuario introduce un número fuera de ese rango, deberá mostrarse un mensaje de advertencia y volver a solicitarse la valoración.

3. Al finalizar, el programa debe:

- Mostrar todas las valoraciones recogidas junto al nombre de cada videojuego.

- Calcular y mostrar la media de todas las valoraciones.

- Indicar cuántos juegos han recibido una valoración mayor o igual a 8.

- Mostrar el videojuego con la mejor valoración y el que tenga la peor.

4. Si por algún motivo no se han podido registrar valoraciones válidas, el programa deberá mostrar un mensaje indicando que no hay datos para analizar.
'''


videojuegos = ["Zelda ToTK", "FIFA 26", "Minecraft", "Call of Duty BO3", "Animal Crossing"]
valoraciones = []
cantidad = len(videojuegos)
i = 0
contador = 0

print("\n=======INTRODUCIR VALORACIONES=======")
while(True):
    if i != cantidad:
        try:
            valoracion = int(input(f"Introduzca una valoración entre 1 y 10 para el videojuego {videojuegos[i]}: "))

            if valoracion <= 0 or valoracion > 10:
                print("Valoración incorrecta, pruebe de nuevo.")
            else:
                valoraciones.append(valoracion)
                i = i + 1
        except:
            print("SOLO SE PERMITEN NÚMEROS DEL 1 al 10")
    else:
        break
    
        

print("\n=======LISTA DE VIDEOJUEGOS + VALORACIONES=======")
for x in range(cantidad):
    print(f"No{x+1}. VALORACIÓN: ({valoraciones[x]}/10) - {videojuegos[x]}")


print("\n=======MEDIA DE TODAS LAS VALORACIONES=======")
valoracionesTotales = sum(valoraciones)
mediaValoraciones = valoracionesTotales / cantidad

print(f"La media de todas las valoraciones es: {mediaValoraciones}")


print("\n=======JUEGOS con VALORACIÓN MAYOR IGUAL a 8=======")
for x in range(cantidad):
    if valoraciones[x] >= 8:
        contador = contador + 1
    
if contador <= 0:
    print("Ningún juego ha recibido una valoración de 8/10 o mayor.")
elif contador == 1:
    print(f"{contador} juego han recibido una valoración de 8/10 o mayor.")
else:
    print(f"{contador} juegos han recibido una valoración de 8/10 o mayor.")
    
posicionMayor = valoraciones.index(max(valoraciones))
posicionMenor = valoraciones.index(min(valoraciones))

print("\n=======MEJOR y PEOR VALORADO=======")
print(f"El primer videojuego mejor valorado de la lista es {videojuegos[posicionMayor]}, con una valoración de {valoraciones[posicionMayor]}")
print(f"El primer videojuego peor valorado de la lista es {videojuegos[posicionMenor]}, con una valoración de {valoraciones[posicionMenor]}")