from stock import Stock, menu_gestion_stock
from Modulo_de_compra import SistemaCompras
from crear_productos import menu
from pagar import realizar_pago

def menu_principal():
    stock = Stock()
    sistema_compras = SistemaCompras(stock)

    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestionar productos")
        print("2. Gestionar stock")
        print("3. Realizar compra")
        print("4. Ver historial de compras")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu(stock)
        elif opcion == "2":
            menu_gestion_stock(stock)
        elif opcion == "3":
            compra = []
            while True:
                producto_id = int(input("Ingrese el ID del producto (0 para finalizar): "))
                if producto_id == 0:
                    break
                cantidad = int(input("Ingrese la cantidad a comprar: "))
                compra.append({"producto_id": producto_id, "cantidad": cantidad})
            sistema_compras.realizar_compra(compra)
        elif opcion == "4":
            sistema_compras.mostrar_historial_compras()
        elif opcion == "5":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu_principal()