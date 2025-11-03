import json

class Tarea:
    
    def __init__(self, titulo, descripcion="", prioridad="Media", fecha_vencimiento=None, completada = False):
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento
        self.completada = completada
    
    def marcar_completada(self):
        self.completada = True
    
    def actualizar(self, titulo=None, descripcion=None, prioridad=None, fecha_vencimiento=None):
        if titulo is not None:
            self.titulo = titulo
        if descripcion is not None:
            self.descripcion = descripcion
        if prioridad is not None:
            self.prioridad = prioridad
        if fecha_vencimiento is not None:
            self.fecha_vencimiento = fecha_vencimiento
    
    def mostrar_informacion(self, imprimir=True):
        estado = "Completada" if self.completada == True else "Pendiente"
        fecha = self.fecha_vencimiento if self.fecha_vencimiento is not None else "Sin fecha"
        
        info = f"""
        \n      ---------------------------
        Título: {self.titulo}
        Descripción: {self.descripcion}
        Prioridad: {self.prioridad}
        Fecha: {fecha}
        Estado: {estado}
        -----------------------------
        """
        
        if imprimir:
            print(info)
        
        return info
    
    def to_dict(self):
        return {
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "prioridad": self.prioridad,
            "fecha": self.fecha_vencimiento,
            "completada": self.completada
        }
        
    
    def __str__(self):
        estado = "Completada" if self.completada == True else "Pendiente"
        fecha = self.fecha_vencimiento if self.fecha_vencimiento is not None else "Sin fecha"
        
        print(f"{self.titulo} | {self.descripcion} - Prioridad: {self.prioridad} ({fecha}) [{estado}]")


class GestorTareas:
    
    def __init__(self):
        self.tareas = []
    
    def agregar_tarea(self, tarea: Tarea):
        self.tareas.append(tarea)
    
    def buscar_tarea_por_titulo(self, titulo):
        for t in self.tareas:
            if t.titulo == titulo:
                return t
    
    def eliminar_tarea(self, titulo):
        t = self.buscar_tarea_por_titulo(titulo)
        
        if not t:
            print("No existe la tarea.")
            return False
        self.tareas.remove(t)
        return True
    
    def actualizar_tarea(self, titulo, nuevo_titulo=None, descripcion=None, prioridad=None, fecha_vencimiento=None):
        t = self.buscar_tarea_por_titulo(titulo)
        
        if not t:
            print("No existe la tarea.")
            return False
        t.actualizar(nuevo_titulo, descripcion, prioridad, fecha_vencimiento)
        return True
    
    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas en la lista.")
            return
        
        PRIORIDAD_VALOR = {"Alta": 1, "Media": 2, "Baja": 3}
        #ordena por estado primero y luego por prioridad
        
        tareas_ordenadas = sorted(self.tareas, key=lambda t:(t.completada, PRIORIDAD_VALOR.get(t.prioridad, 100))) # esto coge el valor mínimo que salga
        
        for t in tareas_ordenadas:
            t.mostrar_informacion()
    
    def guardar_tareas(self, archivo="tareas.json"):
        
        if not self.tareas:
            print("No hay tareas para guardar.")
            return
        else:
            try:
                with open(archivo, "w", encoding="utf-8") as f:
                    data = [t.to_dict() for t in self.tareas]
                    json.dump(data, f, indent=4, ensure_ascii=False)
                print("Archivo guardado con éxito.")
            except Exception as e:
                print(f"Error al guardar el archivo: {e}")
    
    def cargar_tareas(self, archivo="tareas.json"):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.tareas = [Tarea(**t) for t in data]
            print("Archivo cargado con éxito")
        except FileNotFoundError:
            print("Archivo no encontrado")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")


def menu():
    print("\n===== GESTIÓN DE TAREAS =====")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Actualizar tarea")
    print("5. Eliminar tarea")
    print("6. Guardar tareas en JSON")
    print("7. Cargar tareas desde JSON")
    print("0. Salir")


# --- Tests rápidos ---
if __name__ == "__main__":
    gestor = GestorTareas()
    
    while True:
        menu()
        opcion = input("\nElige una opción: ").strip()
        
        if opcion == "1":
            titulo = input("Título: ")
            descripcion = input("Descripción: ")
            prioridad = input("Prioridad (Baja/Media/Alta): ")
            fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ")
            
            tarea = Tarea(titulo, descripcion, prioridad, fecha_vencimiento)
            gestor.agregar_tarea(tarea)
            print("✅ Tarea agregada con exito.")
        
        elif opcion == "2":
            gestor.listar_tareas()
        
        elif opcion == "3":
            titulo = input("Título de la tarea a marcar como completada: ")
            t = gestor.buscar_tarea_por_titulo(titulo)
            if t:
                t.marcar_completada()
                print("✅ Tarea marcada como completada.")
            else:
                print(f"⚠️ No se encontró la tarea '{titulo}'")
        
        elif opcion == "4":
            titulo = input("Título de la tarea a actualizar: ")
            nuevo_titulo = input("Nuevo título: ") or None
            descripcion = input("Descripción: ") or None
            prioridad = input("Prioridad (Baja/Media/Alta): ") or None
            fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ") or None
            
            if gestor.actualizar_tarea(titulo, nuevo_titulo, descripcion, prioridad, fecha_vencimiento):
                print("✅ Tarea actualizada con exito.")
        
        elif opcion == "5":
            titulo = input("Título de la tarea a eliminar: ")
            if gestor.eliminar_tarea(titulo):
                print("✅ Tarea eliminada con exito.")
        
        elif opcion == "6":
            gestor.guardar_tareas()
        
        elif opcion == "7":
            gestor.cargar_tareas()
        
        elif opcion == "0":
            print("Exit.")
            break
        
        else:
            print("Opción no válida.")