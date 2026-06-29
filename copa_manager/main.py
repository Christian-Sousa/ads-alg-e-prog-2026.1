from persistencia import carregar_selecoes, salvar_selecoes, carregar_jogadores, salvar_jogadores
from selecoes import cadastrar_nova_selecao, exibir_selecoes
from jogadores import cadastrar_novo_jodador, listar_jogadores, filtrar_jogadores, exibir_jogadores
from utils import ordenar_dicionarios, eh_decrescente, buscar_nome, filtrar_atributo, sucesso, limpar_tela
from utils import status_copa, existencia_id, listar_por_id, exibir_nome_por_id, filtrar_atributo_int

def main():
    limpar_tela()

    selecoes = carregar_selecoes('selecoes.txt')
    jogadores = carregar_jogadores('jogadores.txt')

    print('='*75)
    print('         ⚽ COPA MANAGER 2026 - FIFA ⚽')
    print('='*75)

    input('Pressione <Enter> para continuar...')
    #selecoes, jogadores, partida = status_copa(s,j,p)
    #print(f'Status: {selecoes} selecoes | {jogadores} jogadores | {partidas} partidas')
    menu = f'''
    --- SELEÇÕES ---
        1. Cadastrar seleção
        2. Listar/Ordenar seleções
        3. Buscar seleção
        4. Filtrar por grupo ou confederação

    --- JOGADORES ---
        5. Cadastrar jogador (vinculado a uma seleção)
        6. Listar / ordenar jogadores
        7. Filtrar jogadores
        8. Artilheiros e estatísticas (média de idade, total de gols)

    --- PARTIDAS ---
        9. Cadastrar partida
        10. Listar partidas
        11. Tabela de classificação por grupo

    --- SISTEMA ---
        12. Salvar dados em arquivo
        0. Sair

=============================================================================

        Escolha uma opção: '''

    opcao_menu = int(input(menu))

    while opcao_menu != 0:
        if opcao_menu==1:
            nova_selecao = cadastrar_nova_selecao()
            selecoes.append(nova_selecao)
            sucesso()

        if opcao_menu==2:
            atributo = input('Ordenar por qual atributo? ')
            ordenacao = int(input('Ordem (1 - Crescente / 2 - Decrescente): '))
            lista_ordenada = ordenar_dicionarios(selecoes, atributo, eh_decrescente(ordenacao))
            exibir_selecoes(lista_ordenada)

        if opcao_menu==3:
            termo = input('Insira o nome(ou parte dele) da seleção que deseja buscar: ')
            buscados = buscar_nome(selecoes, termo)
            exibir_selecoes(buscados)
            
        if opcao_menu==4:
            atributo = input('Filtrar por grupo/confederacao: ')
            termo = input('Insira o nome do grupo/confederacao que deseja buscar: ')
            filtrados = filtrar_atributo(selecoes, termo, atributo)
            exibir_selecoes(filtrados)
        
        if opcao_menu == 5:
            listar_por_id(selecoes)
            id_selecao = int(input('Digite o id da seleção: '))
            existe = existencia_id(selecoes, id_selecao)
            while not existe:
                print('Seleção do jogador não encontrada')
                id_selecao = int(input('Digite o id da seleção novamente: '))
                existe = existencia_id(selecoes, id_selecao)
            nome_jogador, novo_jogador = cadastrar_novo_jodador(id_selecao)
            jogadores.append(novo_jogador)
            print(f"Jogador '{nome_jogador}' cadastrado e vinculado a selecao '{exibir_nome_por_id(selecoes,id_selecao)}'!")

        if opcao_menu == 6:
            criterio = input('Ordenar por qual atributo? ')
            ordem = int(input('Ordem (1 - Crescente / 2 - Decrescente): '))
            if ordem == 1:
                ordem = False
            else:
                ordem = True
            listados = listar_jogadores(jogadores, selecoes, criterio, ordem)
            exibir_jogadores(listados, selecoes)
            
        if opcao_menu == 7:
            posicao = input('Posição (Enter para ignorar): ').strip()
            if posicao == '':
                posicao = None

            idade_min = input('Idade mínima (Enter para ignorar): ').strip()
            if idade_min == '':
                idade_min = None
            else:
                idade_min = int(idade_min)

            idade_max = input('Idade máxima (Enter para ignorar): ').strip()
            if idade_max == '':
                idade_max = None
            else:
                idade_max = int(idade_max)

            parte_nome_selecao = input('Parte do nome da seleção (Enter para ignorar): ').strip()
            if parte_nome_selecao == '':
                parte_nome_selecao = None
                
            filtrados = filtrar_jogadores(jogadores, selecoes, posicao, idade_min, idade_max, parte_nome_selecao)
            exibir_jogadores(filtrados, selecoes)

        if opcao_menu == 8:
            ...

        input('Pressione <Enter> para continuar...')
        opcao_menu = int(input(menu))
    salvar_selecoes('selecoes.txt',selecoes)
    salvar_jogadores('jogadores.txt',jogadores)

main()