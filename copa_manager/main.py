from persistencia import carregar_selecoes, salvar_selecoes
from persistencia import carregar_jogadores, salvar_jogadores
from persistencia import carregar_partidas, salvar_partidas
from selecoes import cadastrar_nova_selecao, exibir_selecoes,obter_id_selecoes_por_nome
from jogadores import cadastrar_novo_jodador, filtrar_jogadores, exibir_jogadores, encontrar_artilheiro
from jogadores import buscar_jogadores_por_selecao_id, total_gols_selecao, media_idade_jogadores_selecao
from partidas import cadastrar_partida, listar_partidas
from utils import ordenar_dicionarios, eh_decrescente, buscar_nome, filtrar_atributo, sucesso, limpar_tela
from utils import status_copa, existencia_id, listar_por_id, exibir_nome_por_id

def main():
    limpar_tela()

    selecoes = carregar_selecoes('selecoes.txt')
    jogadores = carregar_jogadores('jogadores.txt')
    partidas = carregar_partidas('partidas.txt')

    print('='*75)
    print('         ⚽ COPA MANAGER 2026 - FIFA ⚽')
    print('='*75)

    input('Pressione <Enter> para continuar...')
    s, j, p = status_copa(selecoes, jogadores, partidas)
    print(f'\nStatus: {s} selecoes | {j} jogadores | {p} partidas\n')
    menu = f'''
    --- SELEÇÕES ---
        1. Cadastrar seleção
        2. Listar/Ordenar seleções
        3. Buscar seleção
        4. Filtrar por grupo ou confederação
        5. Número de gols de uma seleção

    --- JOGADORES ---
        6. Cadastrar jogador (vinculado a uma seleção)
        7. Listar / ordenar jogadores
        8. Filtrar jogadores
        9. Mostrar artilheiro
        10. Exibir jogadores de um seleção
        11. Média de idade dos jogadores de uma seleção

    --- PARTIDAS ---
        12. Cadastrar partida
        13. Listar partidas
        14. Tabela de classificação por grupo

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
        
        if opcao_menu==5:
            nome_selecao = input('Insira o nome da seleção: ').upper()
            id_selecao = obter_id_selecoes_por_nome(selecoes,nome_selecao)
            selecao_escolhida = buscar_jogadores_por_selecao_id(jogadores, id_selecao)
            total_gols = total_gols_selecao(selecao_escolhida)
            print('\n','-' * 70)
            print(f"A seleção '{nome_selecao}' possui {total_gols} gols no campeonato.")
            print('-' * 70,'\n')

        if opcao_menu == 6:
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

        if opcao_menu == 7:
            criterio = input('Ordenar por qual atributo? ')
            ordenacao = int(input('Ordem (1 - Crescente / 2 - Decrescente): '))
            listados = ordenar_dicionarios(jogadores, criterio, eh_decrescente(ordenacao))
            exibir_jogadores(listados, selecoes)
            
        if opcao_menu == 8:
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

        if opcao_menu == 9:
            artilheiro, gols = encontrar_artilheiro(jogadores)
            print('\nARTILHEIRO ATUAL DA COPA DO MUNDO 2026:')
            print('-' * 70)
            print('Jogador: ', artilheiro)
            print('Total de gols: ', gols)
            print('-' * 70, '\n')

        if opcao_menu == 10:
            nome_selecao = input('Insira o nome da seleção: ')
            id_selecao = obter_id_selecoes_por_nome(selecoes,nome_selecao)
            selecao_escolhida = buscar_jogadores_por_selecao_id(jogadores, id_selecao)
            exibir_jogadores(selecao_escolhida, selecoes)
        
        if opcao_menu == 11:
            nome_selecao = input('Insira o nome da seleção: ').upper()
            id_selecao = obter_id_selecoes_por_nome(selecoes,nome_selecao)
            selecao_escolhida = buscar_jogadores_por_selecao_id(jogadores, id_selecao)
            media_idade = media_idade_jogadores_selecao(selecao_escolhida)
            print('\n','-' * 70)
            print(f"A média de idade dos jogadores da seleção '{nome_selecao}' é {media_idade}")
            print('-' * 70,'\n')

        if opcao_menu == 12:
            nova_partida = cadastrar_partida()
            partidas.append(nova_partida)
            sucesso()

        if opcao_menu == 13:
            listar_partidas(partidas)

        if opcao_menu == 14:
            continue

        input('Pressione <Enter> para continuar...')
        opcao_menu = int(input(menu))
    salvar_selecoes('selecoes.txt',selecoes)
    salvar_jogadores('jogadores.txt',jogadores)
    salvar_partidas('partidas.txt',partidas)
    print(f'\nStatus: {s} selecoes | {j} jogadores | {p} partidas\n')

main()