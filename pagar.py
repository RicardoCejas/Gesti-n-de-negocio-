# COMO (comprador-vendedor)
# QUIERO (Hacer uso de los metodos de pago)
# PARA (Cerrar una operación)

"""
Título: Selección de Método de Pago
Yo, como comprador registrado,
quiero seleccionar mi método de pago preferido durante el proceso de compra,
para que pueda completar mi compra de manera rápida y segura utilizando mi método de pago favorito.
"""

"""
Dado que el comprador está en el proceso de finalizar una compra,
Cuando el sistema muestra las opciones de pago disponibles,
Entonces el comprador debe poder seleccionar su método de pago preferido.

Dado que el comprador ha seleccionado un método de pago,
Cuando el comprador confirma la selección y procede al pago,
Entonces el sistema debe procesar el pago de manera segura.

Dado que el comprador tiene métodos de pago almacenados,
Cuando el comprador desea utilizar uno de ellos,
Entonces el sistema debe permitirle seleccionar, gestionar o eliminar métodos de pago previamente guardados.

Dado que el comprador selecciona un método de pago inválido o sin fondos,
Cuando intenta procesar el pago,
Entonces el sistema debe mostrar un mensaje de error claro y permitirle seleccionar otro método de pago.

Dado que el comprador ha completado la selección del método de pago,
Cuando se confirme el pago,
Entonces el sistema debe proceder con la compra y mostrar una confirmación.
"""

from abc import ABC, abstractmethod

class MetodoDePago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass

# Clase para pagos con Débito
class Debito(MetodoDePago):
    def __init__(self, numero_tarjeta, saldo):
        self.numero_tarjeta = numero_tarjeta
        self.saldo = saldo

    def procesar_pago(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            print(f"Pago de {monto} procesado con Débito. Saldo restante: {self.saldo}")
        else:
            print("Saldo insuficiente para procesar el pago con Débito.")

# Clase para pagos con Crédito
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

# Clase para pagos con Transferencia
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

# Clase para pagos con Efectivo
class Efectivo(MetodoDePago):
    def procesar_pago(self, monto):
        print(f"Pago de {monto} procesado con Efectivo.")

# Función para seleccionar el método de pago
def seleccionar_metodo_pago():
    print("Seleccione el método de pago:")
    print("1. Débito")
    print("2. Crédito")
    print("3. Transferencia")
    print("4. Efectivo")
    print("5. Salir")
    
    opcion = input("Ingrese el número de la opción: ")
    return opcion

# Función para procesar los pagos
def realizar_pago():
    while True:
        opcion = seleccionar_metodo_pago()

        if opcion == '5':
            print("Saliendo del sistema.")
            break  # Salir del ciclo y terminar el programa

        monto = float(input("Ingrese el monto a pagar: "))

        if opcion == '1':  # Débito
            numero_tarjeta = input("Ingrese el número de la tarjeta de débito: ")
            saldo = float(input("Ingrese el saldo disponible: "))
            metodo_pago = Debito(numero_tarjeta, saldo)
            metodo_pago.procesar_pago(monto)

        elif opcion == '2':  # Crédito
            numero_tarjeta = input("Ingrese el número de la tarjeta de crédito: ")
            limite_credito = float(input("Ingrese el límite de crédito disponible: "))
            metodo_pago = Credito(numero_tarjeta, limite_credito)
            metodo_pago.procesar_pago(monto)

        elif opcion == '3':  # Transferencia
            numero_cuenta = input("Ingrese el número de la cuenta bancaria: ")
            saldo = float(input("Ingrese el saldo disponible en la cuenta: "))
            metodo_pago = Transferencia(numero_cuenta, saldo)
            metodo_pago.procesar_pago(monto)

        elif opcion == '4':  # Efectivo
            metodo_pago = Efectivo()
            metodo_pago.procesar_pago(monto)

        else:
            print("Opción no válida, intente nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    realizar_pago()

