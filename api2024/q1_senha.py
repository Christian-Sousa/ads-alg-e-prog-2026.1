import random

def gerar_senha_valida(n):
    if n <= 0:
        return "Tamanho inválido"
    
    senha = []
    
    while len(senha) < n:
        digito = random.randint(0, 9)
        
        if len(senha) == 0:
            # O primeiro dígito pode ser qualquer um
            senha.append(digito)
        else:
            anterior = senha[-1]
            # Regras: 
            # 1. Não pode ser igual ao anterior
            # 2. Não pode ser sucessor (anterior + 1)
            # 3. Não pode ser antecessor (anterior - 1)
            if digito != anterior and digito != anterior + 1 and digito != anterior - 1:
                senha.append(digito)
    
    # Converte a lista de números em uma string única
    return "".join(map(str, senha))

def iniciar_gerador():
    print("--- Gerador de Senhas Numéricas Seguras ---")
    
    try:
        tamanho = int(input("Digite o tamanho desejado para a senha (N): "))
    except ValueError:
        print("Por favor, insira um número inteiro válido.")
        return

    satisfeito = False
    while not satisfeito:
        senha_sugerida = gerar_senha_valida(tamanho)
        print(f"\nSenha sugerida: {senha_sugerida}")
        
        resposta = input("Você está satisfeito com esta senha? (S/N): ").strip().upper()
        
        if resposta == 'S':
            print("Senha definida com sucesso!")
            satisfeito = True
        elif resposta == 'N':
            print("Gerando uma nova opção...")
        else:
            print("Resposta inválida, por favor digite 'S' para sim ou 'N' para não.")

if __name__ == "__main__":
    iniciar_gerador()