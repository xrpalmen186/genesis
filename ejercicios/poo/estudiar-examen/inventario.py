import json

class Producto:
    def __init__(self, nombre, precio, stock, categoria="General"):
        self.nombre = nombre
        self.precio = float(precio)
        self.stock = int(stock)
        self.categoria = categoria

    def actualizar(self, nombre=None, precio=None, stock=None, categoria=None):
        if nombre is not None:
            self.nombre = nombre
        if precio is not None:
            self.precio = float(precio)
        if stock is not None:
            self.stock = int(stock)
        if categoria is not None:
            self.categoria = categoria

    def mostrar(self, imprimir=True):
        info = f"""
--------------------------
Producto: {self.nombre}
Categoria: {self.categoria}
Precio: {self.precio} €
Stock: {self.stock}
--------------------------
"""
        if imprimir:
            print(info)
        return info
    
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "categoria": self.categoria
        }


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def buscar(self, nombre):
        for p in self.productos:
            if p.nombre.lower() == nombre.lower():
                return p

    def eliminar(self, nombre):
        p = self.buscar(nombre)
        if not p:
            print(" Producto no encontrado.")
            return False
        self.productos.remove(p)
        return True

    def actualizar(self, nombre, nuevo_nombre=None, precio=None, stock=None, categoria=None):
        p = self.buscar(nombre)
        if not p:
            print(" Producto no encontrado.")
            return False
        p.actualizar(nuevo_nombre, precio, stock, categoria)
        return True

    def listar(self):
        if not self.productos:
            print(" No hay productos en inventario.")
            return
        for p in self.productos:
            p.mostrar()

    # --- MÉTRICAS Y ESTADÍSTICAS ---

    def producto_mas_caro(self):
        if not self.productos:
            print("No hay productos")
            return
        p = max(self.productos, key=lambda x: x.precio)
        print(" Producto más caro:")
        p.mostrar()

    def producto_mas_barato(self):
        if not self.productos:
            print("No hay productos")
            return
        p = min(self.productos, key=lambda x: x.precio)
        print(" Producto más barato:")
        p.mostrar()

    def productos_con_bajo_stock(self, limite=5):
        bajo = [p for p in self.productos if p.stock <= limite]
        print(f" Productos con stock <= {limite}:")
        if not bajo:
            print(" No hay productos con bajo stock.")
        for p in bajo:
            p.mostrar()

    def valor_total_inventario(self):
        total = sum(p.precio * p.stock for p in self.productos)
        print(f" Valor total del inventario: {total:.2f} €")

    def precio_promedio(self):
        if not self.productos:
            print("No hay productos")
            return
        promedio = sum(p.precio for p in self.productos) / len(self.productos)
        print(f" Precio promedio: {promedio:.2f} €")

    # --- Guardar / Cargar JSON ---
    def guardar(self, archivo="inventario.json"):
        try:
            with open(archivo, "w", encoding="utf-8") as f:
                json.dump([p.to_dict() for p in self.productos], f, indent=4, ensure_ascii=False)
            print(" Inventario guardado correctamente.")
        except:
            print(" Error al guardar inventario.")

    def cargar(self, archivo="inventario.json"):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.productos = [Producto(**p) for p in data]
            print(" Inventario cargado correctamente.")
        except FileNotFoundError:
            print(" Archivo no encontrado.")
        except Exception as e:
            print(f" Error al cargar: {e}")



# ---------------- MENU ----------------

def menu():
    print("""
========= INVENTARIO =========
1. Agregar producto
2. Listar productos
3. Actualizar producto
4. Eliminar producto
5. Guardar inventario
6. Cargar inventario
----- ESTADÍSTICAS -----
7. Producto más caro
8. Producto más barato
9. Productos con bajo stock
10. Valor total del inventario
11. Precio promedio
0. Salir
""")

if __name__ == "__main__":
    inv = Inventario()

    while True:
        menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            precio = input("Precio: ")
            stock = input("Stock: ")
            categoria = input("Categoría: ") or "General"
            inv.agregar_producto(Producto(nombre, precio, stock, categoria))
            print(" Producto agregado.")

        elif opcion == "2":
            inv.listar()

        elif opcion == "3":
            nombre = input("Producto a actualizar: ")
            nuevo = input("Nuevo nombre: ") or None
            precio = input("Nuevo precio: ") or None
            stock = input("Nuevo stock: ") or None
            categoria = input("Nueva categoría: ") or None
            inv.actualizar(nombre, nuevo, precio, stock, categoria)

        elif opcion == "4":
            nombre = input("Producto a eliminar: ")
            if inv.eliminar(nombre):
                print(" Eliminado.")

        elif opcion == "5":
            inv.guardar()

        elif opcion == "6":
            inv.cargar()

        elif opcion == "7":
            inv.producto_mas_caro()

        elif opcion == "8":
            inv.producto_mas_barato()

        elif opcion == "9":
            limite = input("Límite de stock (default=5): ")
            inv.productos_con_bajo_stock(int(limite) if limite else 5)

        elif opcion == "10":
            inv.valor_total_inventario()

        elif opcion == "11":
            inv.precio_promedio()

        elif opcion == "0":
            print(" Saliendo...")
            break
        else:
            print(" Opción no válida.")
