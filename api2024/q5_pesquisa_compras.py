def main():
    lista_descricao=[]
    lista_espec=[]
    lista_valor=[]
    while True:
        descricao=input('Descrição: ')
        especificacao=input('Especificação: ')
        valor=float(input('Valor: R$'))
        lista_descricao.append(descricao)
        lista_espec.append(especificacao)
        lista_valor.append(valor)
        continuar=input('Deseja continuar? ').strip().upper()
        if continuar=='NAO':
            break

    print(f'\n——- PESQUISA DE PREÇOS —---')
    for i in range(len(lista_descricao)):
        print(f'{i + 1} - {lista_descricao[i]} ({lista_espec[i]}) R$ {lista_valor[i]:.2f}')
        
    print('—----------------------------------------')
    print(f'Valor total: R$ {sum(lista_valor):.2f}') 
main()