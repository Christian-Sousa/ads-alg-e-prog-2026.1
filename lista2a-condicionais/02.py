def obter_numeros():
    primeiro = int(input("Digite o 1º valor: "))
    segundo = int(input("Digite o 2º valor: "))
    return primeiro, segundo

def verificar_maior(a, b):
    if a>b:
        maior = print(f"O número maior é {a} e o número menor é {b}")
    else:
        maior = print(f"O número maior é {b} e o número menor é {a}")
    return maior

def main():
    n1, n2=obter_numeros()
    return verificar_maior(n1, n2)

main()
