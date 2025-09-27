# EJERCICIOS

'''

# EJERCICIO PROPUESTO 1

Tenemos un texto dónde queremos encontrar palabras clave. Las palabras clave pueden ser hasta 5 y debemos pedirlas al usuario y guadarlas en una lista.

Si el usuario quiere poner menos de 5 palabras clave, deberá escribir "fin" para terminar de introducir datos. Si el usuario introduce números o nada, deberemos eliminarlos de la lista antes de la búsqueda.

En otra lista, debemos guardar el número de veces que aparece cada palabra clave en nuestro texto. Por ejemplo, si la palabra clave son ordenador y portátil y aparecen 5 y 7 veces respectivamente, nuestras listas deberían ser así:
    - keywords = ["ordenador", "portátil"]
    - ocurrencias = [5, 7]

'''



'''

EJERCICIO PROPUESTO 2

Crea una lista con los nombres de tus 5 frutas favoritas.  
Después:  
1. Añade una fruta más al final de la lista.  
2. Inserta una fruta en la segunda posición.  
3. Elimina la primera fruta usando `pop()`.  
4. Elimina una fruta concreta usando `remove()`.  
5. Muestra la lista final.  


'''




'''

EJERCICIO PROPUESTO 3

Un profesor quiere llevar el control de asistencia de sus alumnos.  

1. Pide al usuario que ingrese nombres de alumnos (como máximo 8).  
   - Si el usuario escribe "fin", se deja de pedir nombres antes del máximo.  
   - Si un alumno se repite, no debe añadirse dos veces (controlar con `in` o métodos de lista).  

2. Muestra la lista de alumnos inscritos.  

3. Simula que uno de los alumnos se ha dado de baja:
   - Pide el nombre de un alumno a eliminar y retíralo de la lista si existe.  

4. Finalmente, muestra la lista de alumnos ordenada alfabéticamente en orden ascendente y en orden descendente.  


'''




'''

EJERCICIO PROPUESTO 4

Estás creando un pequeño gestor de tareas.  

1. Pide al usuario que introduzca tareas (texto corto) y guárdalas en una lista `tareas`.  
   - Como máximo se podrán introducir 10 tareas.  
   - El usuario puede escribir "fin" para dejar de introducir antes de llegar al límite.  

2. Muestra el menú siguiente y permite al usuario elegir varias opciones hasta que escriba "salir":  
   - "mostrar": enseña la lista completa de tareas numeradas.  
   - "eliminar": pide un número de tarea y elimínala usando `pop()`.  
   - "priorizar": pide una tarea y muévela al inicio de la lista (usando `remove` + `insert`).  
   - "ordenar": ordena las tareas alfabéticamente (`sort`).  
   - "invertir": invierte el orden actual (`reverse`).  
   - "vaciar": elimina todas las tareas (`clear`).  

3. Cuando el usuario escriba "salir", el programa muestra la lista final de tareas que quedaron registradas.  


'''