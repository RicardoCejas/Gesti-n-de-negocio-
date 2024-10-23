# Clase para pagos con Transferencia

from metodos_pago import MetodoDePago

class Transferencia(MetodoDePago):
    def __init__(self, numero_cuenta, saldo):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def procesar_pago(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            print(f"Pago de {monto} procesado con Transferencia. Saldo restante: {self.saldo}")
        else:
            print("Saldo insuficiente para procesar el pago con Transferencia.")
