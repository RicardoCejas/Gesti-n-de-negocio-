from database import Database
from admin import AdminInterface
from client import ClientInterface

def main():
    db = Database("tienda.db")
    admin_interface = AdminInterface(db)
    client_interface = ClientInterface(db)

    while True:
        print("\n---INICIO---")
        print("--¿Cómo deseas acceder?--")
        print("1. Cliente")
        print("2. Administrador")
        print("3. Salir del programa")

        choice = input("Ingrese su opción: ")

        if choice == '1':
            # En un sistema real, aquí iría la autenticación del cliente
            client_id = 1  # Asumimos un cliente con ID 1 para este ejemplo
            client_interface.client_menu(client_id)
        elif choice == '2':
            # En un sistema real, aquí iría la autenticación del administrador
            admin_interface.admin_menu()
        elif choice == '3':
            print("Gracias por usar nuestro sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

    db.close()

if __name__ == "__main__":
    main()