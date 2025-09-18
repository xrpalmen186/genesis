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