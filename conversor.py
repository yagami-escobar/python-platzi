# PROGRAMA CONVERSOR DE MONEDAS

menu = """
Bienvenido al conversor de Monedas 🤑

1 - Convertir a Dolares
2 - Convertir a Euros
3 - Convertir a Pesos Argentinos

Elige una opción:
"""

opcion = int(input(menu))


def conversor(opcion):
    nsoles = input("¿Cuantos Nuevos Soles tienes?: ")
    nsoles = float(nsoles)
    if opcion == 1:
        tc = 3.83
        dolares = nsoles / tc
        dolares = round(dolares, 2)
        dolares = str(dolares)
        print ("Tienes "+"$"+ dolares + " dólares.")
    elif opcion == 2:
        tc = 4.04
        euros = nsoles / tc
        euros = round(euros, 2)
        euros = str(euros)
        print ("Tienes "+"$"+ euros + " euros.")
    elif opcion == 3:
        tc = 0.033
        pesos_arg = nsoles / tc
        pesos_arg = round(pesos_arg, 2)
        pesos_arg = str(pesos_arg)
        print ("Tienes "+"$"+ pesos_arg + " pesos argentinos.")
    else:
        print ("TC incorrecto !!")
    

conversor(opcion)

# if opcion == 1:
#     conversor(opcion)
# elif opcion == 2:
#     conversor(opcion)
# elif opcion == 3:
#     conversor(opcion)
# else:
#     print ("Ingresa una opción correcta")

