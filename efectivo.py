# Clase para pagos con Efectivo

from metodos_pago import MetodoDePago

class Efectivo(MetodoDePago):
    def procesar_pago(self, monto):
        print(f"Pago de {monto} procesado con Efectivo.")
