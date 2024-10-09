# Clase para pagos con Efectivo
class Efectivo(MetodoDePago):
    def procesar_pago(self, monto):
        print(f"Pago de {monto} procesado con Efectivo.")
