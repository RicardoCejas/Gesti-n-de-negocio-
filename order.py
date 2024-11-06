from datetime import datetime
from models import Order

class OrderManager:
    def __init__(self, db):
        self.db = db

    def create_order(self, user_id, total, payment_method):
        creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.db.execute(
            "INSERT INTO orders (user_id, creation_date, total, payment_method) VALUES (?, ?, ?, ?)",
            (user_id, creation_date, total, payment_method)
        )
        order_id = self.db.fetch_one("SELECT last_insert_rowid()")[0]
        return Order(order_id, user_id, creation_date, total, payment_method)

    def add_order_detail(self, order_id, product_id, quantity, subtotal):
        self.db.execute(
            "INSERT INTO order_details (order_id, product_id, quantity, subtotal) VALUES (?, ?, ?, ?)",
            (order_id, product_id, quantity, subtotal)
        )

    def get_order(self, order_id):
        order_data = self.db.fetch_one("SELECT * FROM orders WHERE id = ?", (order_id,))
        if order_data:
            order = Order(*order_data)
            details = self.db.fetch_all(
                "SELECT p.name, od.quantity, od.subtotal FROM order_details od JOIN products p ON od.product_id = p.id WHERE od.order_id = ?",
                (order_id,)
            )
            for detail in details:
                order.add_detail(*detail)
            return order
        return None