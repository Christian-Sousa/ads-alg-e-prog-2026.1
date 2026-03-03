def obter_numeros():
    numero = int(input("Digite o 1º valor de dois dígitos: "))
    return numero

def verificar_digitos(a):
    dezena = a//10
    unidade =a%10
    if dezena == unidade:
        print("Os algarismos das dezenas e das unidades são iguais.")
    else:
        print("Os algarismos das dezenas e das unidades são diferentes.")
    return print()

def main():
    n1=obter_numeros()
    return verificar_digitos(n1)

main()