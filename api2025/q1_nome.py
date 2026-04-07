from utils_io import limpar_tela

def main():
    limpar_tela()
    
    tamanho_nome = len(input('Nome: '))
    
    if tamanho_nome%2!=0:
        print(f'divisores de {tamanho_nome}')
        for i in range(1,tamanho_nome+1):
            if tamanho_nome%i==0:
                print(f'{i}', end=',')
    else:
        print(f'os {tamanho_nome} primeiros multiplos de {tamanho_nome}: ')
        for i in range(0,tamanho_nome*tamanho_nome):
            if i%tamanho_nome==0:
                print(f'{i}',end=',')
main()