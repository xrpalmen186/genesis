

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

tareas = []

for x in range(10):
   nuevaTarea = input("Añade una nueva tarea (fin para terminar): ")
   
   if nuevaTarea == "fin":
      break
   else:
      tareas.append(nuevaTarea)

print(tareas)

while(True):
   print("""
         ========================
         1. Mostrar
         2. Eliminar
         3. Priorizar
         4. Ordenar
         5. Invertir
         6. Vaciar
         ........................
         7. Salir
         ========================
         """)
   opcion = input("Introduce una opción (0-7): ")

   if opcion == "1":
      for x in range(len(tareas)):
         print(f"{x+1}. {tareas[x]}")
   elif opcion == "2":
      eliminar = input("Introduzca el número de la tarea a eliminar: ")
      tareas.pop(int(eliminar)+1)
   elif opcion == "3":
      priorizar = input("Introduzca el número de la tarea a priorizar: ")
      tareaPriorizada = tareas.pop(tareas.index(tareas[int(priorizar) - 1]))
      tareas.insert(0, tareaPriorizada)
   elif opcion == "4":
      tareas.sort()
   elif opcion == "5":
      tareas.reverse()
   elif opcion == "6":
      tareas.clear()
   elif opcion == "7":
      print(tareas)
      break
   else:
      print("Opción no válida.")
