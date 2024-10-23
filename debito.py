# Clase para pagos con Débito
from metodos_pago import MetodoDePago

class Debito(MetodoDePago): # type: ignore
    def __init__(self, numero_tarjeta, saldo):
        self.numero_tarjeta = numero_tarjeta
        self.saldo = saldo

    def procesar_pago(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            print(f"Pago de {monto} procesado con Débito. Saldo restante: {self.saldo}")
        else:
            print("Saldo insuficiente para procesar el pago con Débito.")
