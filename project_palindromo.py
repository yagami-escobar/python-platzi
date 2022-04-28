
def palindromo(p_frase):
    p_frase = p_frase.replace(' ', '')
    p_frase = p_frase.lower()
    p_frase_inv = p_frase[::-1]

    if p_frase == p_frase_inv:
        return True
    else:
        return False


def run():
    frase = input("Ingresa tu frase: ")
    is_pal = palindromo(frase)

    if is_pal == True:
        print("Es palindromo")
    else:
        print("No es palindromo")


if __name__ == '__main__':
    run()