def run():
    my_dictionary = {
        'key1': 1,
        'key2': 2,
        'key3': 3
    }
    print(my_dictionary)

    print()
    # IMPRIMIR CON FOR
    my_people = {
        'Perú': 302365,
        'Colombia': 123456,
        'Ecuador': 19865
    }

    for i in my_people.keys():
        print(i)
    print()
    for i in my_people.values():
        print(i)
    print()
    for i, j in my_people.items():
        print(i + ' tiene ' + str(j) + ' habitantes.')

if __name__ == '__main__':
    run()