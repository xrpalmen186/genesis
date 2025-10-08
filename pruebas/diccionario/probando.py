def mostrar_empleados(empleados):
    for empleado in empleados:
        print(f"Empleado: {empleado["nombre"]} - Departamento: {empleado["departamento"]}")
        for proyecto in empleado["proyectos"]:
            print(f"Proyecto: {proyecto['nombre']} - Horas: {proyecto['horas']} - Nota: {proyecto['nota']}")

def filtrar_empleados(empleados, departamento):
    filtrados = [emp["nombre"] for emp in empleados if emp["departamento"].lower() == departamento.lower()]
    return filtrados if filtrados else "No hay empleados en ese departamento."


def filtrar_por_nota(empleados):
    proyectos_buenos = []
    for emp in empleados:
        for p in emp["proyectos"]:
            if p["nota"] >= 8:
                proyectos_buenos.append(p["nombre"])
    # Evitamos duplicados con set
    return list(set(proyectos_buenos))


def media_notas_empleado(empleados):
    medias = {}
    for emp in empleados:
        notas = [p["nota"] for p in emp["proyectos"]]
        medias[emp["nombre"]] = round(sum(notas) / len(notas), 2)
    return medias


def proy_max_horas(empleados):
    horas_por_proyecto = {}
    for emp in empleados:
        for p in emp["proyectos"]:
            horas_por_proyecto[p["nombre"]] = horas_por_proyecto.get(p["nombre"], 0) + p["horas"]

    # Encontramos el proyecto con más horas
    proyecto_max = max(horas_por_proyecto, key=horas_por_proyecto.get)
    return f"{proyecto_max} ({horas_por_proyecto[proyecto_max]} horas en total)"


def main():
    empleados = [
        {
            "nombre": "Ana",
            "departamento": "Marketing",
            "proyectos": [
                {"nombre": "Campaña Redes", "horas": 25, "nota": 8.5},
                {"nombre": "Informe SEO", "horas": 15, "nota": 7.2}
            ]
        },
        {
            "nombre": "Daniel",
            "departamento": "Informatica",
            "proyectos": [
                {"nombre": "Software de Gestion", "horas": 40, "nota": 9},
                {"nombre": "Chat Bot", "horas": 70, "nota": 8.7}
            ]
        },
        {
            "nombre": "Sofia",
            "departamento": "Direccion y Recursos Humanos",
            "proyectos": [
                {"nombre": "Informe de Ventas", "horas": 30, "nota": 8.9},
                {"nombre": "Informe de socios", "horas": 20, "nota": 9.1}
            ]
        },
        {
            "nombre": "Carla",
            "departamento": "Marketing",
            "proyectos": [
                {"nombre": "Campaña Redes", "horas": 12, "nota": 5.1},
                {"nombre": "Informe SEO", "horas": 60, "nota": 3.2}
            ]
        },
        {
            "nombre": "Marta",
            "departamento": "Direccion y Recursos Humanos",
            "proyectos": [
                {"nombre": "Informe de Bienestar", "horas": 40, "nota": 6.5},
                {"nombre": "Informe de Clima Laboral", "horas": 50, "nota": 4.2}
            ]
        }
    ]
    #1 Mostrar todos los empleados con sus proyectos.
    mostrar_empleados(empleados)
    #2 Filtrar empleados de un departamento concreto.
    nomDepartamento=input("¿Que departamento buscas?: ")
    print(f"Los empleados de {nomDepartamento} son :{filtrar_empleados(empleados,nomDepartamento)}")
    # #3 Mostrar solo los nombres de los proyectos con nota mayor a 8.
    print(f"Los proyectos con una nota igual o mayor a 8 son: {filtrar_por_nota(empleados)}")
    # #4 Calcular el promedio de notas por empleado.
    print(f"La media de las notas de cada empleado son{media_notas_empleado(empleados)}")
    
    # #5 Encontrar el proyecto con más horas totales
    print(f"El proyecto con mas horas es {proy_max_horas(empleados)}")


if __name__ == "__main__":
    main()