# ==================================================
# Métodos de listas en Python
# ==================================================

# Lista base para ejemplos
lenguajes = ["C", "Java", "Python", "JavaScript", "Kotlin", "Ruby", "Rust"]
print("Lista inicial:", lenguajes)

# ==================================================
# 1️. Añadir elementos
# ==================================================

# Añadir al final
lenguajes.append("TypeScript")
print("\nappend ->", lenguajes)

# Insertar en una posición concreta
lenguajes.insert(1, "C++")
print("insert ->", lenguajes)

# Extender con otra lista
frameworks = ["Angular", "Vue", "React"]
lenguajes.extend(frameworks)
print("extend ->", lenguajes)


# ==================================================
# 2. Eliminar elementos
# ==================================================
frutas = ["plátano", "kiwi", "papaya", "melocotón", "cereza"]
print("\nFrutas iniciales:", frutas)

# Eliminar por índice (y retorna el valor eliminado)
print("pop() elimina:", frutas.pop())  # último
print("Después de pop:", frutas)

print("pop(0) elimina:", frutas.pop(0))  # primero
print("Después de pop(0):", frutas)

# Eliminar por valor (primer valor que encuentre)
frutas.remove("papaya")
print("remove('papaya') ->", frutas)

# Eliminar usando "del" que es una palabra reservada
del frutas[0]
print("del frutas[0] ->", frutas)

# Vaciar lista (la elimina completamente)
frutas.clear()
print("clear ->", frutas)


# ==================================================
# 3. Buscar elementos
# ==================================================
frutas = ["manzana", "pera", "cereza", "pera"]
print("\nFrutas:", frutas)

# Posición del primer elemento con ese valor
print("index('cereza') ->", frutas.index("cereza"))

# Contar cuántas veces aparece un valor
print("count('pera') ->", frutas.count("pera"))


# ==================================================
# 4. Copiar listas
# ==================================================
copia = frutas.copy()
print("\ncopy ->", copia)


# ==================================================
# 5️. Ordenar y revertir
# ==================================================
numeros = [3, 1, 4, 2]
print("\nNúmeros iniciales:", numeros)

# Ordenar
numeros.sort()
print("sort ->", numeros)

numeros.sort(reverse=True)
print("sort(reverse=True) ->", numeros)

# Invertir orden actual
numeros.reverse()
print("reverse ->", numeros)


# ==================================================
# Resumen rápido
# ==================================================
print("""
Resumen de métodos principales:
--------------------------------
append(x)      -> Añade un elemento al final
insert(i, x)   -> Inserta en la posición i
extend(lista)  -> Añade todos los elementos de otra lista
pop([i])       -> Elimina y devuelve el elemento en i (último si no se pasa)
remove(x)      -> Elimina el primer elemento con valor x
del lista[i]   -> Elimina el elemento en la posición i
clear()        -> Vacía la lista
index(x)       -> Devuelve el índice del primer x
count(x)       -> Cuenta cuántas veces aparece x
copy()         -> Crea una copia de la lista
sort()         -> Ordena la lista
reverse()      -> Invierte el orden de los elementos
""")