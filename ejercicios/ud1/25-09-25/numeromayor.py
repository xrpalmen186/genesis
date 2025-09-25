# 25/09/2025 - Haciendo ejercicios sueltos en clase.

a = int(input("Primer número: "))
b = int(input("Segundo número: "))

if a > b:
    print(f"El primer número ({a}) es mayor que el segundo número ({b}).")
    for i in range(b,a+1):
        print(i)
elif b > a:
    print(f"El segundo número ({b}) es mayor que el primer número ({a}).")
    for i in range(a,b+1):
        print(i)
else:
    print(f"Los dos números son iguales.")


media = (a + b)/2
print(f"La media es {media}")

# que el usuario pueda meter elementos en la lista

lista = []
cantidad = int(input("¿Cuántos elementos quieres añadir en la lista?: "))
cantidad = cantidad + 1

for i in range(1, cantidad):
    num = int(input(f"Número (nº{i}): "))
    lista.append(num)

#media de los números de la lista
media = sum(lista)/len(lista) #también se podría usar "cantidad"
print(lista)
print(f"Media de los valores de la lista: {media}")

#pide un numero, para buscar en la lista, "el 3 está en la posición ..."
buscar = int(input("Introduce un número a buscar en la lista: "))

if buscar in lista:
        i = lista.index(buscar) + 1
        print(f"El número {buscar} está en la posición {i}")
else:
    print("No está en la lista.")
    

#ordenación de la lista
print(f"Lista desordenada: {lista}")
lista.sort()
print(f"Lista ordenada: {lista}")


#dos listas, ordenarlas y unirlas en una sola
lista1 = [1, 60, 20, 45, 3]
lista2 = [24, 25, 9, 2]
nuevalista = []

lista1.sort()
lista2.sort()

print(f"Lista1 ordenada: {lista1}")
print(f"Lista2 ordenada: {lista2}")

lista1.extend(lista2)
lista1.sort()

print(f"Lista completa ordenada: {lista1}")
