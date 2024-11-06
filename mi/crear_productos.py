# Clase Producto
from stock import Stock
from typing import Dict

class Producto:
    def __init__(self, id: int, nombre: str, precio: float):
        self.id = id
        self.nombre = nombre
        self.precio = precio

class Stock:
    def __init__(self):
        self.inventario: Dict[int, int] = {}  # {id_producto: cantidad}
        self.productos: Dict[int, Producto] = {}

    def agregar_producto(self, nombre: str, precio: float, cantidad_inicial: int = 0):
        id = len(self.productos) + 1
        nuevo_producto = Producto(id, nombre, precio)
        self.productos[id] = nuevo_producto
        self.inventario[id] = cantidad_inicial
        print(f"Producto agregado: ID {id}, Nombre: {nombre}, Precio: ${precio}, Stock inicial: {cantidad_inicial}")

    def actualizar_stock(self, producto_id: int, cantidad: int):
        if producto_id in self.inventario:
            self.inventario[producto_id] += cantidad
            print(f"Stock actualizado para el producto {producto_id}. Nuevo stock: {self.inventario[producto_id]}")
        else:
            print(f"El producto con ID {producto_id} no existe.")

    def verificar_stock(self, producto_id: int, cantidad: int) -> bool:
        return self.inventario.get(producto_id, 0) >= cantidad

    def obtener_stock(self, producto_id: int) -> int:
        return self.inventario.get(producto_id, 0)

    def listar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            print("Productos disponibles:")
            for producto in self.productos.values():
                stock = self.obtener_stock(producto.id)
                print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio: ${producto.precio}, Stock: {stock}")

    def eliminar_producto(self, producto_id: int):
        if producto_id in self.productos:
            del self.productos[producto_id]
            del self.inventario[producto_id]
            print(f"Producto con ID {producto_id} eliminado del sistema.")
        else:
            print(f"El producto con ID {producto_id} no existe.")

class Tienda:
    def __init__(self, stock: Stock):
        self.stock = stock

    def agregar_producto(self, nombre, precio, cantidad):
        self.stock.agregar_producto(nombre, precio, cantidad)
        print(f"Producto '{nombre}' agregado con éxito.")

    def mostrar_productos(self):
        self.stock.listar_productos()

def menu_gestion_stock(stock: Stock):
    while True:
        print("\n--- Menú de Gestión de Stock ---")
        print("1. Actualizar stock de un producto")
        print("2. Ver stock actual")
        print("3. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            producto_id = int(input("Ingrese el ID del producto: "))
            cantidad = int(input("Ingrese la cantidad a agregar al stock (use números negativos para restar): "))
            stock.actualizar_stock(producto_id, cantidad)
        elif opcion == "2":
            stock.listar_productos()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def menu(stock: Stock):
    stock = Stock()
    tienda = Tienda(stock)

    while True:
        print("\n--- Gestión de Productos ---")
        print("1. Agregar producto")
        print("2. Ver productos")
        print("3. Gestionar stock")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del producto: ")
            while True:
                try:
                    precio = float(input("Ingrese el precio del producto: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido para el precio.")
            
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad del producto: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido para la cantidad.")
            
            tienda.agregar_producto(nombre, precio, cantidad)

        elif opcion == '2':
            tienda.mostrar_productos()

        elif opcion == '3':
            menu_gestion_stock(stock)

        elif opcion == '4':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
            
# Ejecutar el menú
if __name__ == "__main__":
    menu()