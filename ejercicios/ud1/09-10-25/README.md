# 🎬 Proyecto de Python: Gestión de Reservas de un Cine

## 🧾 Descripción

Este proyecto consiste en desarrollar un sistema en Python para la **gestión de reservas en un cine**. El sistema permitirá gestionar una cartelera de películas, realizar reservas de entradas, buscar películas, guardar y cargar datos desde archivos, y mostrar estadísticas de uso.

Está diseñado para aplicar los conocimientos adquiridos sobre:

- Tipos de datos (listas, diccionarios)
- Funciones y modularización
- Estructuras de control
- Ficheros (JSON y TXT)
- Gestión de errores
- Argumentos arbitrarios (`*args` y `**kwargs`) ✅

---

## 📚 Requisitos del sistema

El programa deberá cumplir los siguientes objetivos:

### 1. Mostrar la cartelera
Crear una función que muestre todas las películas con su título, año, género y horarios disponibles.

### 2. Buscar películas por género o año
Permitir al usuario buscar películas filtrando por `genero` o `anio`. Se debe implementar una función que reciba el criterio de búsqueda como parámetro y devuelva una lista de películas coincidentes.

### 3. Reservar entradas
El usuario podrá seleccionar una película y un horario para hacer una reserva a su nombre. El sistema debe registrar cuántas veces cada usuario ha reservado una película en un horario determinado.

Ejemplo:
```python
reservas = {
    "16:00": {
        "juan": 2,
        "ana": 1
    },
    ...
}
```

### 4. Mostrar estadísticas de usuarios

Calcular cuántas entradas ha reservado cada usuario en total (sumando todas las películas y horarios).

### 5. Guardar y cargar cartelera (JSON)

Permitir guardar la cartelera (con sus reservas) en un fichero `.json`, y cargarla desde un fichero.

### 6. Exportar resumen de cartelera (TXT)

Generar un fichero `.txt` con un resumen legible de todas las películas, horarios y número de reservas por horario.

### 7. Uso de `*args` y `**kwargs` ✅

Crear una función llamada `informacion_peliculas(*args, **kwargs)` que sirva para mostrar información adicional sobre películas recibidas como argumentos arbitrarios.

* `*args`: Recibe múltiples títulos de películas.
* `**kwargs`: Recibe información extra como `idioma="Español"`, `subtitulada=True`, `formato="3D"`.

Esta función **no es parte del flujo principal**, pero debe incluirse en el código para practicar los argumentos arbitrarios.

Ejemplo de uso:

```python
informacion_peliculas("Interstellar", "Coco", idioma="Español", subtitulada=True, formato="3D")
```

Salida esperada:

```
Películas seleccionadas: Interstellar, Coco
Información adicional:
  - idioma: Español
  - subtitulada: True
  - formato: 3D
```

---

## ✨ Estructura de datos sugerida

```python
cartelera = [
    {
        "titulo": "Interstellar",
        "anio": 2014,
        "genero": "Ciencia Ficción",
        "horarios": ["16:00", "19:00", "22:00"],
        "reservas": {
            "16:00": {},
            "19:00": {},
            "22:00": {}
        }
    },
    ...
]
```

---

## 🔧 Funciones sugeridas

| Función                                                 | Descripción                                   |
| ------------------------------------------------------- | --------------------------------------------- |
| `mostrar_cartelera(cartelera)`                          | Muestra todas las películas                   |
| `buscar_pelicula(cartelera, criterio, valor)`           | Busca películas por género o año              |
| `reservar_entrada(cartelera, titulo, horario, usuario)` | Registra una reserva                          |
| `estadisticas_reservas(cartelera)`                      | Devuelve diccionario con total por usuario    |
| `guardar_cartelera(cartelera, fichero)`                 | Guarda la cartelera en JSON                   |
| `cargar_cartelera(fichero)`                             | Carga la cartelera desde JSON                 |
| `exportar_resumen(cartelera, fichero_txt)`              | Exporta un resumen legible en `.txt`          |
| `informacion_peliculas(*args, **kwargs)`                | Función para practicar `*args` y `**kwargs` ✅ |

---

## 🧪 Flujo del programa principal (`main()`)

1. Crear una cartelera inicial con 3 o más películas.
2. Mostrar la cartelera actual.
3. Permitir búsqueda por género o año.
4. Permitir realizar reservas múltiples.
5. Mostrar estadísticas de reservas por usuario.
6. Guardar la cartelera en un fichero `.json`.
7. Cargar la cartelera desde un fichero `.json`.
8. Exportar resumen a `.txt`.
9. Demostrar uso de la función `informacion_peliculas(*args, **kwargs)`.

---

## 📂 Ejemplo de resumen `.txt`

```
--- RESUMEN CARTELERA ---

Película: Interstellar (2014)
Género: Ciencia Ficción
Horario 16:00 - Reservas: 2
Horario 19:00 - Reservas: 0
Horario 22:00 - Reservas: 1

Película: Coco (2017)
Género: Animación
Horario 18:00 - Reservas: 1
Horario 21:00 - Reservas: 0
```

---

## 📌 Notas finales

* Usa `try/except` para evitar errores al trabajar con ficheros.
* Usa `input()` para pedir al usuario información.
* Organiza tu código en funciones, y no pongas toda la lógica en el `main()`.