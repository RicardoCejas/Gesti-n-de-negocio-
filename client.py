from models import Client, Cart, Product
from order import OrderManager
from invoice import generate_invoice

class ClientInterface:
    def __init__(self, db):
        self.db = db
        self.cart = Cart()
        self.order_manager = OrderManager(db)

    def view_products(self):
        products = self.db.fetch_all("SELECT * FROM products")
        for product in products:
            print(f"ID: {product[0]}, Nombre: {product[1]}, Precio: ${product[2]}, Cantidad: {product[3]}, Unidad: {product[4]}")

    def add_to_cart(self, product_id, quantity):
        product = self.db.fetch_one("SELECT * FROM products WHERE id = ?", (product_id,))
        if product:
            self.cart.add_item(Product(product[0], *product[1:]), quantity)
            print(f"{quantity} {product[1]} added to cart")
        else:
            print("Product not found")

    def view_cart(self):
        for product, quantity in self.cart.items.items():
            print(f"{product.name}: {quantity} x ${product.price} = ${quantity * product.price}")
        print(f"Total: ${self.cart.get_total()}")

    def checkout(self, client_id):
        if not self.cart.items:
            print("Your cart is empty")
            return

        print("--Con qué método desea pagar--")
        print("1. Efectivo")
        print("2. Transferencia")
        print("3. Débito")
        print("4. Crédito")

        payment_method = input("Ingrese su opción de pago: ")
        payment_methods = {
            '1': 'Efectivo',
            '2': 'Transferencia',
            '3': 'Débito',
            '4': 'Crédito'
        }

        if payment_method not in payment_methods:
            print("Método de pago inválido")
            return

        total = self.cart.get_total()
        order = self.order_manager.create_order(client_id, total, payment_methods[payment_method])

        for product, quantity in self.cart.items.items():
            self.order_manager.add_order_detail(order.order_id, product.id, quantity, product.price * quantity)

        generate_invoice(order, self.cart.items)
        self.cart = Cart()  # Clear the cart after checkout
        print("Compra realizada con éxito. Se ha generado su factura.")

    def client_menu(self, client_id):
        while True:
            print("\n---Tienda---")
            print("--Elija qué productos desea comprar--")
            self.view_products()
            product_id = input("Ingrese el ID del producto que desea comprar (o 'q' para salir): ")
            
            if product_id.lower() == 'q':
                break

            try:
                product_id = int(product_id)
                quantity = int(input("Ingrese la cantidad: "))
                self.add_to_cart(product_id, quantity)
            except ValueError:
                print("Por favor, ingrese un número válido.")

            add_more = input("¿Desea agregar otro producto? (si/no): ")
            if add_more.lower() != 'si':
                break

        self.view_cart()
        checkout = input("¿Desea proceder con la compra? (si/no): ")
        if checkout.lower() == 'si':
            self.checkout(client_id)