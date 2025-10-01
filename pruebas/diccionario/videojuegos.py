

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

print(nombres)
print(valoraciones)


# Repaso de diccionarios y listas. Clase 1/10/25

asignatura1 = {"nombre":"serv", "profesor":"JI", "horas":7}
asignatura2 = {"nombre":"clie", "profesor":"David", "horas":6}
notas = {"mates":9, "servidor":4}

persona = {"nombre":"Ray", "edad":19, "asignaturas":[asignatura1, asignatura2], "notas":notas}

alumnos = []
alumnos.append(persona)

print(alumnos[0]["asignaturas"][0]["horas"])

#media de las notas

media = sum(notas.values()) / len(notas)
print(media)

#programa que permita meter otro alumno

alumno2 = {}

alumno2["nombre"] = input("Nombre: ")
alumno2["edad"] = int(input("Edad: "))
alumno2["asignaturas"] = []
alumno2["asignaturas"].append(asignatura1)
alumno2["asignaturas"].append(asignatura2)
alumno2["notas"] = notas

alumnos.append(alumno2)

print(alumnos)

# cuando se recorre un diccionario pero no se especifica ni si es por values o keys por cual recorre por defecto?

# Solucion: 

for alumno in alumnos:
    print(alumno["nombre"])
    print(alumno["edad"])
    print(alumno["asignaturas"])
    print(alumno["notas"])

# se recorre por las keys

for alumno in alumnos:
    for key in alumno:
        print(alumno[key])


i = 0
for a in alumnos:
    x = list(a["notas"].values())
    print(f"Media de {a['nombre']} es {sum(x)/len(x)}")
    print(f"Media de {a['notas']} es {sum(a['notas'].values()) / len(a['notas'])}")
    print(f"Suspensos de {a['nombre']} es {len([x for x in a['notas'].values() if x < 5])}")
    print(f"Asignaturas suspensas de {a['nombre']} es {len([x for x in a['asignaturas'] if x[i] < 6])}")
    i += 1