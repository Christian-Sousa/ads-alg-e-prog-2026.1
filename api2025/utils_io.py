import os

def limpar_tela():
    # 'nt' refere-se ao Windows, 'posix' a Linux/macOS
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
