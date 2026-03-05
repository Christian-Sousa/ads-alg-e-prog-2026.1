def obter_numeros(numero):
    return int(input(numero))

def calcular(valor1,valor2):
    if valor1%valor2 == 1:
        return print(f"A soma dessas variáveis mais o resto da divisão: {valor1+valor2+1}")
    elif valor1%valor2 == 2:
        if valor1%2==0:
            resultado1 = "par"
        else:
            resultado1 = "impar"
    
        if valor2%2==0:
            resultado2 = "par"
        else:
            resultado2 = "impar"
        return print(f"Se o primeiro e o segundo valor são pares ou ímpares: {resultado1},{resultado2}")
    elif valor1%valor2 == 3:
        return print(f"multiplicação da soma dos valores lidos pelo primeiro: {(valor1+valor2)*valor1}")
    elif valor1%valor2 == 4:
        return print(f"Divisão da soma dos números lidos pelo segundo: {(valor1+valor2)/valor2}")
    else:
        return print(f"O quadrado dos números lidos: {valor1**2,valor2**2}")
    
def main():
    n1 = obter_numeros("Primeiro número: ")
    n2 = obter_numeros("Segundo número: ")
    return calcular(n1,n2)

main()
    

    