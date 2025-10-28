# 
# --------------------------------------------
# GESTIÓN DE RESERVAS DE UN CINE - PLANTILLA
# --------------------------------------------
# Autor: [Tu Nombre]
# Curso: Python 3
# Nivel: Sin orientación a objetos

import json

# ------------------------------
# FUNCIÓN 1: Mostrar la cartelera
# ------------------------------
def mostrar_cartelera(cartelera):
    """UT2.1.5: Aplicación Python Personal
    Muestra todas las películas disponibles en la cartelera.
    """
    pass


# ---------------------------------------------------
# FUNCIÓN 2: Buscar película por género o por año
# ---------------------------------------------------
def buscar_pelicula(cartelera, criterio, valor):
    """
    Busca películas según un criterio ('genero' o 'anio') y valor dado.
    Retorna lista de títulos encontrados.
    """
    pass


# ------------------------------------------
# FUNCIÓN 3: Reservar entrada para un usuario
# ------------------------------------------
def reservar_entrada(cartelera, titulo, horario, usuario):
    """
    Registra una reserva de entrada para un usuario en una película y horario.
    Si ya reservó, aumenta el contador.
    """
    pass


# ---------------------------------------------
# FUNCIÓN 4: Estadísticas de reservas por usuario
# ---------------------------------------------
def estadisticas_reservas(cartelera):
    """
    Devuelve un diccionario con total de reservas por usuario.
    """
    pass


# --------------------------------------
# FUNCIÓN 5: Guardar cartelera (JSON)
# --------------------------------------
def guardar_cartelera(cartelera, nombre_fichero):
    """
    Guarda la cartelera completa (con reservas) en un fichero JSON.
    """
    pass


# ------------------------------------
# FUNCIÓN 6: Cargar cartelera (JSON)
# ------------------------------------
def cargar_cartelera(nombre_fichero):
    """
    Carga la cartelera desde un fichero JSON.
    Devuelve la lista de películas cargada.
    """
    pass


# -----------------------------------------------
# FUNCIÓN 7: Exportar resumen en archivo de texto
# -----------------------------------------------
def exportar_resumen(cartelera, nombre_fichero):
    """
    Exporta un resumen legible de la cartelera y reservas a un archivo .txt
    """
    pass


# ---------------------------------------------------
# FUNCIÓN 8: Usar *args y **kwargs para mostrar info
# ---------------------------------------------------
def informacion_peliculas(*args, **kwargs):
    """
    Muestra los títulos de películas pasados como *args
    y la información adicional pasada como **kwargs
    """
    pass


# --------------------------------------------
# PROGRAMA PRINCIPAL
# --------------------------------------------
def main():
    # Crear una cartelera inicial con al menos 3 películas
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
        {
            "titulo": "Coco",
            "anio": 2017,
            "genero": "Animación",
            "horarios": ["18:00", "21:00"],
            "reservas": {
                "18:00": {},
                "21:00": {}
            }
        },
        {
            "titulo": "Gladiator",
            "anio": 2000,
            "genero": "Acción",
            "horarios": ["17:00", "20:00"],
            "reservas": {
                "17:00": {},
                "20:00": {}
            }
        }
    ]

    # 1. Mostrar cartelera
    mostrar_cartelera(cartelera)

    # 2. Buscar películas por criterio
    criterio = input("Buscar por 'genero' o 'anio': ").lower()
    valor = input("Introduce el valor: ")
    if criterio == 'anio':
        valor = int(valor)
    peliculas_encontradas = buscar_pelicula(cartelera, criterio, valor)
    print(f"Películas encontradas: {peliculas_encontradas}")

    # 3. Realizar reservas
    cantidad = int(input("¿Cuántas reservas quieres hacer?: "))
    for _ in range(cantidad):
        titulo = input("Título de la película: ")
        horario = input("Horario: ")
        usuario = input("Nombre del usuario: ")
        reservar_entrada(cartelera, titulo, horario, usuario)

    # 4. Mostrar estadísticas de reservas
    estadisticas = estadisticas_reservas(cartelera)
    print("Estadísticas de reservas:", estadisticas)

    # 5. Guardar cartelera en JSON
    nombre_fichero_guardar = input("Nombre del fichero JSON para guardar: ")
    guardar_cartelera(cartelera, nombre_fichero_guardar)

    # 6. Cargar cartelera desde JSON
    nombre_fichero_cargar = input("Nombre del fichero JSON para cargar: ")
    cartelera_cargada = cargar_cartelera(nombre_fichero_cargar)
    if cartelera_cargada:
        print("Cartelera cargada correctamente.")
        mostrar_cartelera(cartelera_cargada)

    # 7. Exportar resumen a TXT
    nombre_resumen = input("Nombre del fichero resumen TXT: ")
    exportar_resumen(cartelera, nombre_resumen)

    # 8. Usar *args y **kwargs
    informacion_peliculas(
        "Interstellar", "Coco", idioma="Español", subtitulada=True, formato="3D"
    )


# Ejecutar solo si es el archivo principal
if __name__ == "__main__":
    main()