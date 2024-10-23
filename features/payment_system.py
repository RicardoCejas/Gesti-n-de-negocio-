class PaymentSystem:
    def __init__(self):
        self.available_payment_methods = ["Credit Card", "Debit Card", "PayPal", "Bank Transfer"]
        self.saved_payment_methods = []
        self.selected_payment_method = None
        self.payment_confirmed = False

    def show_payment_methods(self):
        return self.available_payment_methods

    def save_payment_method(self, method):
        if method in self.available_payment_methods:
            self.saved_payment_methods.append(method)
            return f"Payment method {method} saved."
        return "Invalid payment method."

    def select_payment_method(self, method):
        if method in self.available_payment_methods:
            self.selected_payment_method = method
            return f"Payment method {method} selected."
        return "Invalid payment method."

    def confirm_payment(self):
        if self.selected_payment_method:
            self.payment_confirmed = True
            return "Payment confirmed."
        return "No payment method selected."

    def handle_invalid_payment(self):
        return "Error: Invalid payment method or insufficient funds."

    def get_saved_methods(self):
        return self.saved_payment_methods
