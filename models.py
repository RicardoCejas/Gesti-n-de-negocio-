from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, phone, address, email):
        self.name = name
        self.phone = phone
        self.address = address
        self.email = email

    @abstractmethod
    def update_profile(self, db, **kwargs):
        pass

class Administrator(User):
    def __init__(self, name, phone, address, email, admin_id):
        super().__init__(name, phone, address, email)
        self.admin_id = admin_id

    def update_profile(self, db, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        
        db.execute('''
        UPDATE users
        SET name = ?, phone = ?, address = ?, email = ?
        WHERE id = ?
        ''', (self.name, self.phone, self.address, self.email, self.admin_id))

class Client(User):
    def __init__(self, name, phone, address, email, client_id):
        super().__init__(name, phone, address, email)
        self.client_id = client_id

    def update_profile(self, db, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        
        db.execute('''
        UPDATE users
        SET name = ?, phone = ?, address = ?, email = ?
        WHERE id = ?
        ''', (self.name, self.phone, self.address, self.email, self.client_id))

class Product:
    def __init__(self, id, name, price, quantity, unit):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.unit = unit

class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def update_quantity(self, product, quantity):
        if product in self.items:
            self.items[product] = quantity
        else:
            raise ValueError("Product not in cart")

    def remove_item(self, product):
        if product in self.items:
            del self.items[product]
        else:
            raise ValueError("Product not in cart")

    def get_total(self):
        return sum(product.price * quantity for product, quantity in self.items.items())

class Order:
    def __init__(self, order_id, user_id, creation_date, total, payment_method):
        self.order_id = order_id
        self.user_id = user_id
        self.creation_date = creation_date
        self.total = total
        self.payment_method = payment_method
        self.details = []

    def add_detail(self, product, quantity, subtotal):
        self.details.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })