from persistencia import carregar_partidas, carregar_selecoes
from utils import gerar_id,listar_por_id
from selecoes import obter_id_selecoes_por_nome,obter_nome_selecoes_por_id

partidas = carregar_partidas('partidas.txt')
selecoes = carregar_selecoes('selecoes.txt')

def cadastrar_partida():
    listar_por_id(selecoes)
    selecao_casa = input('Nome da seleção DENTRO DE CASA: ')
    selecao_casa_id = int(obter_id_selecoes_por_nome(selecoes, selecao_casa))
    selecao_fora = input('Nome da seleção FORA DE CASA: ')
    selecao_fora_id = int(obter_id_selecoes_por_nome(selecoes, selecao_fora))
    gols_casa = int(input(f'Gols da seleçao {selecao_casa}: '))
    gols_fora = int(input(f'Gols da seleçao {selecao_fora}: '))
    fase = input('Fase do campeonato: ')
    nova_partida  = {
         'id':gerar_id(partidas, 5001),
         'selecao_casa_id': selecao_casa_id,
         'selecao_fora_id': selecao_fora_id,
         'gols_casa': gols_casa,
         'gols_fora': gols_fora,
         'fase': fase,
        }
    return nova_partida

def listar_partidas(partidas):
    for p in partidas:
        casa_nome = obter_nome_selecoes_por_id(selecoes, p['selecao_casa_id'])
        fora_nome = obter_nome_selecoes_por_id(selecoes, p['selecao_fora_id'])
        fase = p['fase']
        print('\n','-'*70,'\n')
        print(f'{casa_nome}({p['gols_casa']}) x ({p['gols_fora']}){fora_nome}({fase})')
        print('\n','-'*70,'\n')

