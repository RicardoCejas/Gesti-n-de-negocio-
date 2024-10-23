# Clase Producto
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Cantidad en stock: {self.cantidad}")
        print("-" * 30)

# Clase Tienda para gestionar los productos
class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        nuevo_producto = Producto(nombre, precio, cantidad)
        self.productos.append(nuevo_producto)
        print(f"Producto '{nombre}' agregado con éxito.")

    def mostrar_productos(self):
        if len(self.productos) == 0:
            print("No hay productos disponibles.")
        else:
            print("Lista de productos:")
            for producto in self.productos:
                producto.mostrar_informacion()

# Función principal
def menu():
    tienda = Tienda()

    while True:
        print("\n--- Gestión de Productos ---")
        print("1. Agregar producto")
        print("2. Ver productos")
        print("3. Salir")
        
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
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecutar el menú
if __name__ == "__main__":
    menu()
