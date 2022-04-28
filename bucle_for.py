def run():
    print("***** Imprime la Lista del Rango *****")
    rango = list(range(10))
    print(rango)

    print()
    print("***** FOR (10) *****")
    for i in range(10):
        print(i)

    print()
    print("***** RECORRIENDO UN STRING *****")
    cadena = "npm --version"
    
    for j in cadena:
        print(j)

if __name__ == '__main__':
    run()