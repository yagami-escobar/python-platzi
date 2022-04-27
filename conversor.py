# PROGRAMA CONVERSOR DE MONEDAS

menu = """
Bienvenido al conversor de Monedas 🤑

1 - Convertir a Dolares
2 - Convertir a Euros
3 - Convertir a Pesos Argentinos

Elige una opción:
"""

opcion = input(menu)


if opcion == '1':
    nsoles = input("¿Cuantos Nuevos Soles tienes?: ")
    nsoles = float(nsoles)
    tc_dolares = 3.83
    dolares = nsoles / tc_dolares
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print ("Tienes "+"$"+ dolares + " dólares.")
elif opcion == '2':
    nsoles = input("¿Cuantos Nuevos Soles tienes?: ")
    nsoles = float(nsoles)
    tc_euros = 4.04
    euros = nsoles / tc_euros
    euros = round(euros, 2)
    euros = str(euros)
    print ("Tienes "+"$"+ euros + " euros.")
elif opcion == '3':
    nsoles = input("¿Cuantos Nuevos Soles tienes?: ")
    nsoles = float(nsoles)
    tc_pesos_arg = 0.033
    pesos_arg = nsoles / tc_pesos_arg
    pesos_arg = round(pesos_arg, 2)
    pesos_arg = str(pesos_arg)
    print ("Tienes "+"$"+ pesos_arg + " pesos argentinos.")
else:
    print ("Ingresa una opción correcta")

