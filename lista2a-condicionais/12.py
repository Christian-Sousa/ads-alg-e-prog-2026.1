def obter_numeros():
    numero = int(input("Digite um número: "))
    return numero

def par_impar():
    numero = obter_numeros()
    if numero%2 == 0:
        resultado = print("O número é par")
    else:
        resultado = print("O número é impar")
    return resultado 

def main():
    exibir = par_impar()
    return exibir

main()