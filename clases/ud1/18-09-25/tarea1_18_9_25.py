#!/usr/bin/python3

a = int(input("Introduce el primer valor: "))
b = int(input("Introduce el segundo valor: "))
suma = a + b
resta = a - b
multi = a * b
divi = a / b

print("El primer valor es:", a)
print("El segundo valor es:", b)
print("######################################")
print("El resultado de la suma es:", suma)
print("El resultado de la resta es:", resta)
print("El resultado de la multiplicacion es:", multi)
print("El resultado de la division es:", divi)

# print("La suma de los dos números es %d" %(a+b))

# print("Suma: %d, Resta: %d" %(a+b,a-b))

'''
Con %d decimos que ese lugar va un decimal, y lo que hay fuera con otro %
es lo que se sustituirá en %d como decimal.
'''

# La manera que nosotros usaremos será la siguiente:

print(f"Suma: {a+b}, Resta: {a-b}")
# Esto interpreta lo que hay entre llaves y meterlo en la misma cadena.



# listas pueden modificar su valor, tupla no puede modificar su valor

l = [1, "hola", 5.9] #lista
meses = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre') #tupla

print(l)
print(meses)

# mapa y diccionarios

d = {'nombre':'Ray', 'edad':19} # diccionario, clave:valor
print(d)

p1 = {'nombre':'JI', 'edad':44} # diccionario, clave:valor
p2 = {'nombre':'Mercedes', 'edad':39} # diccionario, clave:valor
profes = [p1, p2]
print(profes)

# asignaciones múltiples

'''
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)
'''

# intercambiar variables

a = 5
b = 6

a, b = b, a
print(a,b)

# truquitos de la función print

print(1,2,3, sep="-", end=".\n")

# concatenación en cadena
nombre = "Ray"
edad = 19
idprofe = nombre+str(edad)
print(idprofe)




# unir dos listas
l1 = [4, 6, 10]
l2 = [3, 9, 8]
print(l1 + l2, len(l1) + len(l2)) # con "len" vemos el tamaño de la lista

# como salgo del for?? que hago si no encuentra el numero?
l = [1,2,3,4,5]

n = int(input("Dime un número: "))

for i in l:
    if i == n:
        print("Encontrado")
        break
    else:
        print("No encontrado")
        
#