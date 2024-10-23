# Clase para pagos con Crédito

from metodos_pago import MetodoDePago

class Credito(MetodoDePago):
    def __init__(self, numero_tarjeta, limite_credito):
        self.numero_tarjeta = numero_tarjeta
        self.limite_credito = limite_credito

    def procesar_pago(self, monto):
        if self.limite_credito >= monto:
            self.limite_credito -= monto
            print(f"Pago de {monto} procesado con Crédito. Crédito restante: {self.limite_credito}")
        else:
            print("Límite de crédito insuficiente para procesar el pago.")
