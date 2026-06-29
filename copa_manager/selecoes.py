from utils import gerar_id
from persistencia import carregar_selecoes

selecoes = carregar_selecoes('selecoes.txt')

def cadastrar_nova_selecao():
    nome = input('Nome: ')
    confederacao = input('Confederação: ')
    grupo = input('Grupo: ')
    ranking_fifa = int(input('Ranking FIFA: '))
    titulos = int(input('Títulos: '))
    nova_selecao = {
         'id':gerar_id(selecoes, 1),
         'nome':nome,
         'confederacao': confederacao,
         'grupo': grupo,
         'ranking_fifa': ranking_fifa,
         'titulos': titulos,
        }
    return nova_selecao

def obter_nome_selecoes(selecoes,selecao_id):
    for selecao in selecoes:
        if selecao['id'] == selecao_id:
            return selecao['nome']
    return None

def exibir_selecoes(selecoes):
    print('\nLISTA DE SELECOES')
    print('-' * 70)
    for selecao in selecoes:
        print(
            f"Nome: {selecao['nome']}\n"
            f"Confederação: {selecao['confederacao']}\n"
            f"Grupo: {selecao['grupo']}\n"
            f"Ranking FIFA: {selecao['ranking_fifa']}\n"
            f"Títulos: {selecao['   ']}\n"
            f"{'-'*70}"
        )