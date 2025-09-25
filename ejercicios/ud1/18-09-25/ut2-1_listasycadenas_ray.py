#!/usr/bin/env python3

#Raimundo Palma Méndez - UT2.1 Ejercicios Listas y cadenas

#Listas = actividad
#Cadenas = ejercicio


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
    

# EJERCICIO CADENAS    
        
# 1. Crear un programa que lea por teclado una cadena y un carácter, e inserte el carácter entre cada letra de la cadena. Ej: separar y , debería devolver s,e,p,a,r,a,r
def ejercicio1():
    cadena = input("Introduce una cadena: ")
    caracter = input("Introduce un carácter: ")

    #usamos join() para insertar el carácter entre cada letra
    resultado = caracter.join(cadena)

    print("Resultado:", resultado)


# 2. Crear un programa que lea por teclado una cadena y un carácter, y reemplace todos los dígitos en la cadena por el carácter. Ej: su clave es: 1540 y X debería devolver su clave es: XXXX
def ejercicio2():
    cadena = input("Introduce una cadena: ")
    caracter = input("Introduce un carácter: ")

    resultado = ""
    for c in cadena:
        if c.isdigit(): # isdigit() comprueba si el carácter es un número
            resultado += caracter
        else:
            resultado += c

    print("Resultado:", resultado)


# 3. Crea un programa python que lea una cadena de caracteres y muestre la siguiente información:
'''
- La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial Bus debe devolver USB.

- Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe república argentina debe devolver República Argentina.

- Las palabras que comiencen con la letra A. Por ejemplo, si recibe Antes de ayer debe devolver Antes ayer.
'''
def ejercicio3():
    cadena = input("Introduce una frase: ")

    palabras = cadena.split() # separamos en palabras

    # 1. Iniciales
    iniciales = "".join([p[0].upper() for p in palabras]) # primera letra de cada palabra
    print("Iniciales:", iniciales)

    # 2. Cada palabra con primera letra mayúscula
    mayusculas = " ".join([p.capitalize() for p in palabras])
    print("Capitalizadas:", mayusculas)

    # 3. Palabras que comiencen con 'A' o 'a'
    con_a = [p for p in palabras if p.lower().startswith("a")]
    print("Palabras con A:", " ".join(con_a))


# 4. Escribir funciones que dadas dos cadenas de caracteres:
'''
- Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, cadena es una subcadena de subcadena.

- Devuelva la que sea anterior en orden alfabético. Por ejemplo, si recibe kde y gnome debe devolver gnome.
'''
def ejercicio4():
    cadena1 = input("Introduce la primera cadena: ")
    cadena2 = input("Introduce la segunda cadena: ")

    #subcadena
    if cadena2 in cadena1:
        print(f"'{cadena2}' es una subcadena de '{cadena1}'")
    else:
        print(f"'{cadena2}' NO es una subcadena de '{cadena1}'")

    #orden alfabético
    if cadena1 < cadena2:
        print("En orden alfabético va primero:", cadena1)
    else:
        print("En orden alfabético va primero:", cadena2)


# 5. Escribir un programa python que dado una palabra diga si es un palíndromo. Un palídromo Un palíndromo es una palabra, número o frase que se lee igual hacia adelante que hacia atrás. Ejemplo: reconocer.
def ejercicio5():
    palabra = input("Introduce una palabra: ")

    #quitamos espacios y pasamos a minúsculas
    sinespacios = palabra.replace(" ", "").lower()

    if sinespacios == sinespacios[::-1]:
        print(f"'{palabra}' es un palíndromo.")
    else:
        print(f"'{palabra}' NO es un palíndromo.") 




print("\n--- Actividad 1 Listas ---")
actividad1()

print("\n--- Actividad 2 Listas ---")
actividad2()

print("\n--- Actividad 3 Listas ---")
actividad3()

print("\n--- Actividad 4 Listas ---")
actividad4()

print("\n--- Ejercicio 1 Cadenas ---")
ejercicio1()

print("\n--- Ejercicio 2 Cadenas ---")
ejercicio2()

print("\n--- Ejercicio 3 Cadenas ---")
ejercicio3()

print("\n--- Ejercicio 4 Cadenas ---")
ejercicio4()

print("\n--- Ejercicio 5 Cadenas ---")
ejercicio5()