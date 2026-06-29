from utils import gerar_id
from persistencia import carregar_selecoes,carregar_jogadores
from selecoes import obter_nome_selecoes

jogadores = carregar_jogadores('jogadores.txt')
selecoes = carregar_selecoes('selecoes.txt')

def cadastrar_novo_jodador(id_selecao_fk):
    nome = input('Nome do jogador: ')
    posicao = input('Posição do jogador: ')
    idade = int(input('Idade do jogador: '))
    gols = int(input('Quantidade de gols: '))
    novo_jogador = {
         'id': gerar_id(jogadores, 101),
         'nome': nome,
         'selecao_id': id_selecao_fk,
         'posicao': posicao,
         'idade': idade,
         'gols': gols
        }
    return nome, novo_jogador

def listar_jogadores(jogadores, selecoes, criterio, decrescente=False):
    jogadores_ordenados = sorted(jogadores, key=lambda jogador: jogador[criterio], reverse=decrescente)
    return jogadores_ordenados

def filtrar_jogadores(jogadores, selecoes, posicao=None, idade_min=None, idade_max=None, parte_nome_selecao=None):
    filtrados = []

    for jogador in jogadores:
        nome_selecao = obter_nome_selecoes(selecoes, jogador['selecao_id'])

        if posicao is not None:
            if jogador['posicao'].lower() != posicao.lower():
                continue

        if idade_min is not None:
            if jogador['idade'] < idade_min:
                continue

        if idade_max is not None:
            if jogador['idade'] > idade_max:
                continue

        if parte_nome_selecao is not None:
            if parte_nome_selecao.lower() not in nome_selecao.lower():
                continue

        filtrados.append(jogador)

    return filtrados

def exibir_jogadores(jogadores, selecoes):
    print('\nLISTA DE JOGADORES')
    print('-' * 70)
    for jogador in jogadores:
        nome_selecao = obter_nome_selecoes(selecoes, jogador['selecao_id'])

        print(
            f"Nome: {jogador['nome']}\n"
            f"Seleção: {nome_selecao}\n"
            f"Idade: {jogador['idade']}\n"
            f"Gols: {jogador['gols']}\n"
            f"{'-'*70}"
        )