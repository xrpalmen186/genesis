import json
import os

# Archivos
ARCHIVO_CANCIONES = 'canciones.json'
ARCHIVO_USUARIOS = 'usuarios.json'

# Datos cargados
canciones = []
usuarios = []

# -------------------- CARGA Y GUARDADO --------------------

def cargar_datos():
    global canciones, usuarios
    if os.path.exists(ARCHIVO_CANCIONES):
        with open(ARCHIVO_CANCIONES, 'r', encoding='utf-8') as f:
            canciones = json.load(f)
    else:
        canciones = []

    if os.path.exists(ARCHIVO_USUARIOS):
        with open(ARCHIVO_USUARIOS, 'r', encoding='utf-8') as f:
            usuarios = json.load(f)
    else:
        usuarios = []

def guardar_datos():
    with open(ARCHIVO_CANCIONES, 'w', encoding='utf-8') as f:
        json.dump(canciones, f, indent=4, ensure_ascii=False)
    with open(ARCHIVO_USUARIOS, 'w', encoding='utf-8') as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)

# -------------------- FUNCIONES PRINCIPALES --------------------

def mostrar_canciones():
    if not canciones:
        print("No hay canciones registradas.")
        return
    for c in canciones:
        print(f"[{c['id']}] {c['titulo']} - {c['artista']} ({c['anio']}, {c['genero']})")

def añadir_cancion():
    titulo = input("Título: ").strip()
    artista = input("Artista: ").strip()
    anio = int(input("Año: "))
    genero = input("Género: ").strip()
    nuevo_id = max((c['id'] for c in canciones), default=0) + 1
    canciones.append({
        "id": nuevo_id,
        "titulo": titulo,
        "artista": artista,
        "anio": anio,
        "genero": genero
    })
    print("Canción añadida correctamente.")

def buscar_canciones():
    termino = input("Buscar por título o artista: ").strip().lower()
    resultados = [
        c for c in canciones
        if termino in c['titulo'].lower() or termino in c['artista'].lower()
    ]
    if resultados:
        for c in resultados:
            print(f"[{c['id']}] {c['titulo']} - {c['artista']}")
    else:
        print("No se encontraron coincidencias.")

def registrar_usuario():
    nombre = input("Nombre de usuario: ").strip()
    if any(u['nombre_usuario'] == nombre for u in usuarios):
        print("El usuario ya existe.")
        return
    edad = int(input("Edad: "))
    pais = input("País: ").strip()
    usuarios.append({
        "nombre_usuario": nombre,
        "edad": edad,
        "pais": pais,
        "favoritos": {}
    })
    print("Usuario registrado correctamente.")

def añadir_favorito():
    nombre = input("Nombre de usuario: ").strip()
    usuario = next((u for u in usuarios if u['nombre_usuario'] == nombre), None)
    if not usuario:
        print("Usuario no encontrado.")
        return
    try:
        id_cancion = int(input("ID de la canción: "))
        cancion = next(c for c in canciones if c['id'] == id_cancion)
    except (ValueError, StopIteration):
        print("Canción no encontrada.")
        return
    valoracion = float(input("Valoración (0.0 a 10.0): "))
    usuario['favoritos'][str(id_cancion)] = valoracion
    print("Canción añadida/actualizada en favoritos.")

def mostrar_favoritos():
    nombre = input("Nombre de usuario: ").strip()
    usuario = next((u for u in usuarios if u['nombre_usuario'] == nombre), None)
    if not usuario:
        print("Usuario no encontrado.")
        return
    if not usuario['favoritos']:
        print("Este usuario no tiene canciones favoritas.")
        return
    for id_str, val in usuario['favoritos'].items():
        cancion = next((c for c in canciones if c['id'] == int(id_str)), None)
        if cancion:
            print(f"[{cancion['id']}] {cancion['titulo']} - {cancion['artista']} | Valoración: {val}")

def filtrar_canciones():
    opcion = input("¿Filtrar por género (g) o año (a)? ").strip().lower()
    if opcion == 'g':
        genero = input("Género: ").strip().lower()
        filtradas = [c for c in canciones if c['genero'].lower() == genero]
    elif opcion == 'a':
        try:
            anio = int(input("Año: "))
            filtradas = [c for c in canciones if c['anio'] == anio]
        except ValueError:
            print("Año no válido.")
            return
    else:
        print("Opción no válida.")
        return
    if filtradas:
        for c in filtradas:
            print(f"[{c['id']}] {c['titulo']} - {c['artista']}")
    else:
        print("No se encontraron coincidencias.")

def mostrar_estadisticas():
    valoraciones = []
    popularidad = {}

    for usuario in usuarios:
        for id_str, val in usuario['favoritos'].items():
            valoraciones.append(val)
            popularidad[id_str] = popularidad.get(id_str, 0) + 1

    if not valoraciones:
        print("No hay valoraciones disponibles.")
        return

    media = sum(valoraciones) / len(valoraciones)
    print(f"Media general de valoraciones: {media:.2f}")

    # Mejor valorada
    mejor_valorada_id = max(popularidad, key=lambda k: sum(
        u['favoritos'].get(k, 0) for u in usuarios
    ))
    mejor_valorada = next((c for c in canciones if str(c['id']) == mejor_valorada_id), None)

    # Más popular
    mas_popular_id = max(popularidad, key=popularidad.get)
    mas_popular = next((c for c in canciones if str(c['id']) == mas_popular_id), None)

    if mejor_valorada:
        print(f"Canción mejor valorada: {mejor_valorada['titulo']} de {mejor_valorada['artista']}")
    if mas_popular:
        print(f"Canción más popular: {mas_popular['titulo']} de {mas_popular['artista']} ({popularidad[mas_popular_id]} favoritos)")

# -------------------- MENÚ PRINCIPAL --------------------

def menu():
    cargar_datos()
    while True:
        print("\n--- BIBLIOTECA MUSICAL ---")
        print("1. Mostrar todas las canciones")
        print("2. Añadir nueva canción")
        print("3. Buscar canciones por título o artista")
        print("4. Registrar nuevo usuario")
        print("5. Añadir canción a favoritos de un usuario")
        print("6. Mostrar canciones favoritas de un usuario")
        print("7. Filtrar canciones por género o año")
        print("8. Mostrar estadísticas (valoraciones y popularidad)")
        print("9. Guardar y salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            mostrar_canciones()
        elif opcion == "2":
            añadir_cancion()
        elif opcion == "3":
            buscar_canciones()
        elif opcion == "4":
            registrar_usuario()
        elif opcion == "5":
            añadir_favorito()
        elif opcion == "6":
            mostrar_favoritos()
        elif opcion == "7":
            filtrar_canciones()
        elif opcion == "8":
            mostrar_estadisticas()
        elif opcion == "9":
            guardar_datos()
            print("Datos guardados. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# -------------------- EJECUCIÓN --------------------

if __name__ == "__main__":
    menu()
