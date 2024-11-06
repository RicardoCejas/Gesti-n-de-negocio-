from models import Administrator, Product

class AdminInterface:
    def __init__(self, db):
        self.db = db

    def view_products(self):
        products = self.db.fetch_all("SELECT * FROM products")
        for product in products:
            print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Quantity: {product[3]}, Unit: {product[4]}")

    def add_product(self, name, price, quantity, unit):
        self.db.execute(
            "INSERT INTO products (name, price, quantity, unit) VALUES (?, ?, ?, ?)",
            (name, price, quantity, unit)
        )
        print("Product added successfully")

    def update_product(self, product_id, **kwargs):
        set_clause = ', '.join([f"{key} = ?" for key in kwargs.keys()])
        query = f"UPDATE products SET {set_clause} WHERE id = ?"
        values = list(kwargs.values()) + [product_id]
        self.db.execute(query, values)
        print("Product updated successfully")

    def delete_product(self, product_id):
        self.db.execute("DELETE FROM products WHERE id = ?", (product_id,))
        print("Product deleted successfully")

    def admin_menu(self):
        while True:
            print("\n---Administración----")
            print("--¿Que acción desea implementar?--")
            print("1. Ver Productos")
            print("2. Agregar Producto")
            print("3. Actualizar Producto")
            print("4. Eliminar Producto")
            print("5. Volver al menú")

            choice = input("Ingrese su opción: ")

            if choice == '1':
                self.view_products()
            elif choice == '2':
                name = input("Ingrese el nombre del producto: ")
                price = float(input("Ingrese el precio del producto: "))
                quantity = int(input("Ingrese la cantidad del producto: "))
                unit = input("Ingrese la unidad del producto (ml, kg, L, ML, unidad): ")
                self.add_product(name, price, quantity, unit)
            elif choice == '3':
                product_id = int(input("Ingrese el ID del producto a actualizar: "))
                name = input("Ingrese el nuevo nombre del producto (deje en blanco para no cambiar): ")
                price = input("Ingrese el nuevo precio del producto (deje en blanco para no cambiar): ")
                quantity = input("Ingrese la nueva cantidad del producto (deje en blanco para no cambiar): ")
                unit = input("Ingrese la nueva unidad del producto (deje en blanco para no cambiar): ")
                updates = {}
                if name: updates['name'] = name
                if price: updates['price'] = float(price)
                if quantity: updates['quantity'] = int(quantity)
                if unit: updates['unit'] = unit
                self.update_product(product_id, **updates)
            elif choice == '4':
                product_id = int(input("Ingrese el ID del producto a eliminar: "))
                self.delete_product(product_id)
            elif choice == '5':
                break
            else:
                print("Opción inválida. Por favor, intente de nuevo.")