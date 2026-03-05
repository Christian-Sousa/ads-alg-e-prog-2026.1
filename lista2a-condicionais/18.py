def obter_numeros(numero):
    return int(input(numero))

def decodificando_operacoes(n1, n2, numero_operacao):
    if numero_operacao == 1:
        return n1+n2
    elif numero_operacao == 2:
        return n1-n2
    elif numero_operacao == 3:
        return n1*n2
    elif numero_operacao == 4:
        return n1/n2
def main():
    numero1 = obter_numeros("Primeiro número: ")
    numero2 = obter_numeros("Segundo número: ")
    numero_op = obter_numeros("Códido da operação: ")
    print(f"Resultado: {decodificando_operacoes(numero1,numero2,numero_op)}")

main()