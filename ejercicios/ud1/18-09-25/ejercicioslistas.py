#!/usr/bin/env python3

# 1. Lee por teclado números y guardalo en una lista, el proceso finaliza cuando metamos un número negativo. Muestra el máximo de los números guardado en la lista, muestra los números pares.
def actividad1():
    numeros = []
    while True:
        n = int(input("Introduce un número (negativo para salir): "))
        if n < 0:
            break #si es negativo salimos del bucle
        numeros.append(n) #para añadir a la lista
    
    if numeros:
        print("Números introducidos:", numeros)
        print("Máximo:", max(numeros))
        pares = [x for x in numeros if x % 2 == 0]
        print("Números pares:", pares)
    else:
        print("No se introdujeron números válidos.")

# 2. Realizar un programa que, dada una lista, devuelva una nueva lista cuyo contenido sea igual a la original pero invertida. Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’, ‘papa’], deberá devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’].
def actividad2():
    lista = ['Di', 'buen', 'día', 'a', 'papa']
    invertida = lista[::-1]
    print("Lista original:", lista)
    print("Lista invertida:", invertida)

# 3. Dada una lista de cadenas, pide una cadenena por teclado e indica si está en la lista, indica cuantas veces aparece en la lista, lee otra cadena y sustituye la primera por la segunda en la lista, y por último borra la cadena de la lista
def actividad3():
    lista = ["casa", "perro", "gato", "perro", "coche"]
    print("Lista inicial:", lista)
    
    buscar = input("Introduce una cadena para buscar: ")
    if buscar in lista:
        print(f"La cadena '{buscar}' está en la lista.")
        # TODO: lista.count? para decir cuantas veces aparece en la lista
        print(f"Aparece {lista.count(buscar)} veces.")
    else:
        print(f"La cadena '{buscar}' no está en la lista.")
    
    nueva = input("Introduce una cadena nueva para sustituir la primera: ")
    if buscar in lista:
        #sustituir solo la primera
        
        # TODO: nueva = lista.index??
        i = lista.index(buscar)
        lista[i] = nueva
        print("Lista después de la sustitución:", lista)
    
    borrar = input("Introduce una cadena para borrar de la lista: ")
    if borrar in lista:
        # lista = [x for x in lista if x != borrar] ?? no lo entiendo del todo
        print("Lista después de borrar:", lista)
    else:
        print(f"La cadena '{borrar}' no se encuentra en la lista.")

# 4. Dado una lista, hacer un programa que indique si está ordenada o no.
def actividad4():
    lista = [1, 2, 3, 4, 5]
    print("Lista:", lista)
    
    if lista == sorted(lista):
        print("La lista está ordenada de forma ascendente.")
    elif lista == sorted(lista, reverse=True):
        print("La lista está ordenada de forma descendente.")
    else:
        print("La lista no está ordenada.")
        
        

print("\n--- Actividad 1 ---")
actividad1()

print("\n--- Actividad 2 ---")
actividad2()

print("\n--- Actividad 3 ---")
actividad3()

print("\n--- Actividad 4 ---")
actividad4()