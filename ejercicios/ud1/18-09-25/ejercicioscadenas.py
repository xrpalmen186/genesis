#!/usr/bin/env python3

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
        if c.isdigit():        # isdigit() comprueba si el carácter es un número
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

    palabras = cadena.split()   # separamos en palabras

    # 1. Iniciales
    iniciales = "".join([p[0].upper() for p in palabras])  # primera letra de cada palabra
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

    # 1. Subcadena
    if cadena2 in cadena1:
        print(f"'{cadena2}' es una subcadena de '{cadena1}'")
    else:
        print(f"'{cadena2}' NO es una subcadena de '{cadena1}'")

    # 2. Orden alfabético
    if cadena1 < cadena2:
        print("En orden alfabético va primero:", cadena1)
    else:
        print("En orden alfabético va primero:", cadena2)


# 5. Escribir un programa python que dado una palabra diga si es un palíndromo. Un palídromo Un palíndromo es una palabra, número o frase que se lee igual hacia adelante que hacia atrás. Ejemplo: reconocer.
def ejercicio5():
    palabra = input("Introduce una palabra: ")

    # Normalizamos quitando espacios y pasando a minúsculas
    normalizada = palabra.replace(" ", "").lower()

    if normalizada == normalizada[::-1]:
        print(f"'{palabra}' es un palíndromo.")
    else:
        print(f"'{palabra}' NO es un palíndromo.")


while True:
        print("\nElige ejercicio de cadenas: 1, 2, 3, 4, 5  o 0 para salir")
        opcion = input(">>> ")

        if opcion == "1":
            ejercicio1()
        elif opcion == "2":
            ejercicio2()
        elif opcion == "3":
            ejercicio3()
        elif opcion == "4":
            ejercicio4()
        elif opcion == "5":
            ejercicio5()
        elif opcion == "0":
            print("Exit.")
            break
        else:
            print("Opción no válida.")