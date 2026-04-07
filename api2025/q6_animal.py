import math
from utils_io import limpar_tela

def primo(n):
    if n < 2:
        return False
    limite = int(math.sqrt(n))
    for i in range(2, limite + 1):
        if n % i == 0:
            return False        
    return True

def main():
    limpar_tela() 

    nome = input('Nome do animal: ')
    minimo = 7
    while len(nome)<minimo:
        nome = input(f'O nome deve ser maior que {minimo}. -> ')
    
    quantidade = len(nome)
    numeros_recebidos = []
    print(f"O nome '{nome}' tem {quantidade} letras. Digite {quantidade} números.")
    for i in range(quantidade):
        num = int(input(f"Digite o {i+1}º número inteiro: "))

        if primo(num):
            print(f"O número {num} é primo! Interrompendo a leitura...")
            break
        
        numeros_recebidos.append(num)
    
    if numeros_recebidos:
        somatorio = sum(numeros_recebidos)
        media = somatorio / len(numeros_recebidos)
        
        print("\n--- Resultados ---")
        print(f"Números processados: {numeros_recebidos}")
        print(f"Somatório: {somatorio}")
        print(f"Média: {media:.2f}")
    else:
        print("\nNenhum número válido (não primo) foi processado.")

main()