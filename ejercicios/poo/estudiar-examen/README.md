# GestionTareasOO
Programa en python de gestión de tareas con orientación a objetos

## Descripción
Este proyecto implementa un **Sistema de Gestión de Tareas** en Python utilizando el paradigma de **Orientación a Objetos (OOP)**. La aplicación permite a los usuarios crear, actualizar, eliminar y ver tareas, cada una con sus propios atributos, y gestionarlas de forma estructurada.

## Objetivo
El proyecto tiene como objetivo aplicar conceptos clave de **programación orientada a objetos**, como **clases**, **objetos**, **métodos**, **...** en Python. Los estudiantes construirán una herramienta funcional para gestionar tareas, consolidando su comprensión de OOP y otros fundamentos de programación en Python.

## Requerimientos del Proyecto

### Clases y Métodos
1. **Clase `Tarea`**: Representa cada tarea con los siguientes atributos:
   - `titulo`: El título de la tarea.
   - `descripcion`: Breve descripción de la tarea.
   - `prioridad`: Nivel de prioridad (ej., Baja, Media, Alta).
   - `fecha_vencimiento`: Fecha de vencimiento.
   - `completada`: Un valor booleano que indica si la tarea está completada.

   Métodos principales de `Tarea`:
   - `marcar_completada()`: Marca la tarea como completada.
   - `actualizar()`: Actualiza el título, descripción, prioridad, o fecha de vencimiento.
   - `mostrar_informacion()`: Muestra información detallada de la tarea.

2. **Clase `GestorTareas`**: Administra una lista de tareas (`Tarea`) y permite realizar acciones sobre ella:
   - `agregar_tarea()`: Añade una nueva tarea a la lista.
   - `eliminar_tarea()`: Elimina una tarea de la lista por título.
   - `actualizar_tarea()`: Actualiza una tarea específica.
   - `listar_tareas()`: Muestra todas las tareas, organizadas por prioridad y estado de completadas o pendientes.
   - `guardar_tareas()`: Guarda las tareas en un archivo JSON para persistencia.
   - `cargar_tareas()`: Carga las tareas desde un archivo JSON al iniciar el programa.

### Interfaz de Usuario en Consola
Implementa una interfaz en la consola que permita al usuario interactuar con el gestor de tareas mediante un menú. Las opciones incluyen:
- Añadir nueva tarea.
- Marcar tarea como completada.
- Actualizar tarea.
- Ver todas las tareas pendientes.
- Ver todas las tareas completadas.
- Guardar y cargar tareas.