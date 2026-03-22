#lista[numero] -> retorna valor
#lista.index(numero) -> retorna índice

def main():
    lista=[0,1,1,2]
    for i in range (3,1000):
        ultimo_numero = lista[i]
        penultimo_numero = lista[lista.index(ultimo_numero)-1]
        lista.append(ultimo_numero+penultimo_numero)
    
    numeros = int(input('Quantos números da sequência de fibonacci deseja exibir? '))
    if numeros < 2:
        print('''
              > A QUANTIDADE DE VALORES DEVE SER MAIOR OU IGUAL A 2!!!
              ''')
    elif numeros>1000:
        print('> DESCULPE. O LIMITE DE TERMOS DA SEQUENCIA É 1000(MIL)!!!')
    else:
        for i in range(numeros):
            print(lista[i], end="; ")

main()