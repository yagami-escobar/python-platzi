#1
# def imprimir_msg():
#     print ('Mensaje especial: ')
#     print ('¡Estoy aprendiendo a usar funciones!')


# imprimir_msg()
# imprimir_msg()
# imprimir_msg()


#2
# def mensaje(msg):
#     print("Hola, elegiste la opcion:")
#     print(msg)

# opcion = int(input("Elige una opción(1, 2 ,3 ): "))

# if opcion == 1:
#     mensaje(opcion)
# elif opcion == 2:
#     mensaje(opcion)
# elif opcion == 3:
#     mensaje(opcion)
# else:
#     print('Escribe la opción correcta')



print(" BIENVENIDO AL PROGRAMA DE OPERACIONES ARITMETICAS ➕➖➗")

def sumar(a, b):
    print('La suma de' + a + ' y ' + b + ' es:')
    result = a + b
    print(result)

def restar(a, b):
    print('La resta de' + a + ' y ' + b + ' es:')
    result = a - b
    print(result)

def multiplicar(a, b):
    print('El producto de' + a + ' y ' + b + ' es:')
    result = a * b
    print(result)

def dividir(a, b):
    print('La división de' + a + ' y ' + b + ' es:')
    result = a / b
    print(result)

n1 = int(input("Ingrese n1: "))
n2 = int(input("Ingrese n2: "))

menu1 = """"
¿Que operación desea realizar?

1. Suma
2. Resta
3. Producto
4. Division

Elige >>>
"""
opcion = input(menu1)

if opcion == '1':
    sumar(n1, n2)
elif opcion == '2':
    restar(n1, n2)
elif opcion == '2':
    multiplicar(n1, n2)
elif opcion == '2':
    dividir(n1, n2)
else:
    print("Elige una opción correcta !!")
