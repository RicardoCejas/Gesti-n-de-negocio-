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

def modo_de_pago():
    nombre = input("Ingrese su nombre:  ")
    usuario = input("Ingrese la forma de pago que quiere realizar -> Mercado pago, Debito, Credito, Uala, NaranjaX: ")
    if usuario.lower() =='mercado pago':
        print(f"Gracias {nombre} por elegir Mercado pago!!! ")
    elif usuario.lower() == 'debito':
        print(f"Gracias {nombre} por elegir Debito!!! ")
    elif usuario.lower() == 'credito':
        print(f"Gracias {nombre} por elegir Credito!!! ")
    elif usuario.lower() == 'uala':
        print(f"Gracias {nombre} por elegir Uala!!! ")
    elif usuario.lower() == 'naranjax':
        print(f"Gracias {nombre} por elegir NaranjaX!!! ")
    else:
        print("Ingreso incorrectamente ")
        
modo_de_pago()

reinteto = input("Quiere reintentarlo otra vez? (s/n): ")
if reinteto.lower() == 's':
    modo_de_pago()
else:
    print(f"Gracias por usar nuetro modo de pago")
    
def modo_de_pago():
    nombre = input("Ingrese su nombre: ")
    opciones = ['mercado pago', 'debito', 'credito', 'uala', 'naranjax']
    while True:
        usuario = input("Ingrese la forma de pago que quiere realizar -> Mercado pago, Debito, Credito, Uala, NaranjaX: ").lower()
        
        if usuario in opciones:
            print(f"Gracias {nombre} por elegir {usuario.capitalize()}!!!")
        else:
            print("Ingreso incorrecto, por favor intente nuevamente.")
            continue
        
        reintento = input("¿Quiere realizar otra transacción? (s/n): ").lower()
        if reintento != 's':
            print("Gracias por usar nuestro servicio de pago.")
            break

# Llamada a la función
modo_de_pago()
