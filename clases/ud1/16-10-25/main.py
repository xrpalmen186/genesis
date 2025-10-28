import random, json, time

alumnos = []
participados = []

archivoAlumnos = "pendiente.json"
archivoParticipado = "participados.json"

# carga de datos con json
def cargar_alumnos(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            alumnos = json.load(f)
        return alumnos
    except FileNotFoundError:
        print("Archivo no encontrado, creando uno vacio.")
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4, ensure_ascii=False)
        return []
    except:
        print("Error al cargar.")
        return []

def cargar_participados(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            participados = json.load(f)
        return participados
    except FileNotFoundError:
        print("Archivo no encontrado, creando uno vacio.")
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4, ensure_ascii=False)
        return []
    except:
        print("Error al cargar.")
        return []

# guardado de datos
def guardar_alumnos(archivo, alumnos):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(alumnos, f, indent=4, ensure_ascii=False)

def guardar_participados(archivo, participados):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(participados, f, indent=4, ensure_ascii=False)


def elegir_usuario(alumnos):
    if len(alumnos) == 0:
        print("Todos los alumnos han salido.")
        return
    
    # que muestre 5 alumnos al azar cada 1 segundo y el ultimo es el que sale:
    speed = 0.1
    loading = "-"
    
    print("\n")
    
    for i in range(30):
        
        if i == 5:
            loading = "\\"
            speed = 0.12
        elif i == 10:
            loading = "|"
            speed = 0.15
        elif i == 20:
            loading = "/"
            speed = 0.25
        elif i == 25:
            loading = "-"
            speed = 0.45
        elif i == 28:
            loading = "\\"
            speed = 0.75
        elif i == 29:
            loading = "|"
            speed = 1.2
        
        alumno_elegido_muestra = random.choice(alumnos)
        
        print(" " * 50, end="\r")
        print(f" [{loading}]: {alumno_elegido_muestra}", end="\r", flush=True)
        
        # end="\r" hace que el cursor vuelva al inicio de la línea sin saltar a una nueva
        # flush=True fuerza a Python a imprimir inmediatamente (sin esperar al buffer)
        
        time.sleep(speed)
        
    alumno_elegido = random.choice(alumnos)
    alumnos.remove(alumno_elegido)
    participados.append(alumno_elegido)
    guardar_alumnos(archivoAlumnos, alumnos)
    guardar_participados(archivoParticipado, participados)
    print(" " * 50, end="\r")
    print("\n=================ALUMNO ELEGIDO=========================")
    print(f"[+]: {alumno_elegido}")
    print("========================================================\n")

def main():
    alumnos = cargar_alumnos(archivoAlumnos)
    participados = cargar_participados(archivoParticipado)

    while True:
        print("=========================================")
        print("1. Elegir un alumno aleatorio")
        print("2. Mostrar alumnos por salir")
        print("3. Mostrar alumnos que ya han salido")
        print("4. Reiniciar alumnos")
        print("-----------------------------------------")
        print("5. Salir")
        print("=========================================")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            elegir_usuario(alumnos)
        elif opcion == "2":
            print("Alumnos por salir: ")
            for alumno in alumnos:
                print(alumno)
        elif opcion == "3":
            print("Alumnos que ya han salido: ")
            for participado in participados:
                print(participado)
        elif opcion == "4":
            alumnos = cargar_alumnos("lista_alumnos.json")
            participados = []
            guardar_alumnos(archivoAlumnos, alumnos)
            guardar_participados(archivoParticipado, participados)
            print("Los alumnos se han reiniciado.")
        elif opcion == "5":
            break
        else:
            print("Opcion no valida.")
            

if __name__ == "__main__":
    main()