import os

def perfeito(n):
    if n < 2:
        return False
    soma = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            soma +=i # equivalente a: soma = soma + i
            if i != n // i:  # Adiciona o par divisor (ex: se n=28 e i=2, adiciona 14)
                soma += n // i
    return soma == n

def verificar_intervalo_perfeito(n, m):
    inicio = min(n, m)
    fim = max(n, m)
    print(f"Verificando números perfeitos entre {inicio} e {fim}:")
    for num in range(inicio, fim + 1):
        if perfeito(num):
            print(f"{num} é perfeito")
        else:
            print(f"{num} não é perfeito")

def main():
    os.system('cls')
    valor1 = int(input("Digite o valor inicial: "))
    valor2= int(input("Digite o valor final: "))
    verificar_intervalo_perfeito(valor1, valor2)

main()