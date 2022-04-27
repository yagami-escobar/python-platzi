edad = int(input("Escribe tu edad: "))

if edad < 13:
    print('Eres mayor de edad')
elif edad >= 14 and edad <= 17:
    print('Eres un Puber')
elif edad > 17 and edad <=25:
    print('Eres un Joven')
elif edad > 25:
    print('Eres un Adulto')
else:
    print('No temas aún estas a tiempo')

    