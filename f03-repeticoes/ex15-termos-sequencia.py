def main():
    lista = []
    acumulativo=1
    for i in range(0,1000000):
        if i==0:
            acumulativo=acumulativo+i
            lista.append(acumulativo)
        else:
            acumulativo=acumulativo+i+1
            lista.append(acumulativo)
    numeros = int(input('Quantos números da sequência (1,3,6,10,15,...) deseja exibir? '))
    if numeros > 1000000:
        print('> DESCULPE. O LIMITE DE NÚMEROS É 1000000(UM MILHÃO)!!!')
    else:
        for i in range(numeros):
            print(lista[i], end="; ")


main()

#ENUMERATE:
"""
cardapio = ["Suco de Melancia", "Paozinho", "Café"]

for i, item in enumerate(cardapio, start=1):
    print(f"{i}. {item}")
"""