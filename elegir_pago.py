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