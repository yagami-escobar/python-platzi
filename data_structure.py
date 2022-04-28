def run():
    list1 = [1, 2.12, "Jhordan", True, False]
    print("*** LISTA: ***")
    print(list1)
    print()
    print("*** ELEMENTOS: ***")
    print(list1[0])
    print(list1[1])
    print(list1[2])
    print(list1[3])
    print(list1[4])
    print()
    print("*** FUNCIONES LISTAS: ***")
    list1.append(11) #Agregar Elemento
    list1.pop(0)     #Eliminar Elemento 0
    list1[::1]       #Voltear la Lista

if __name__ == '__main__':
    run()