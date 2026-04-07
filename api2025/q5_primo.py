import math
from utils_io import limpar_tela


def primo(n):
    limpar_tela()

    if n < 2:
        return False
    limite = int(math.sqrt(n))
    for i in range(2, limite + 1):
        if n % i == 0:
            return False        
    return True

n_inicial = int(input("Digite o valor de N: "))
m_final = int(input("Digite o valor de M: "))

print(f"Números primos entre {n_inicial} e {m_final}:")

inicio = min(n_inicial, m_final)
fim = max(n_inicial, m_final)

for num in range(inicio, fim + 1):
    if primo(num):
        print(num, end=" ")