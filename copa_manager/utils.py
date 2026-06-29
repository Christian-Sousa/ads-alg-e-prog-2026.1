def limpar_tela():
    import os
    if os.name == 'nt':
          os.system('cls')
    else:
         os.system('clear')

def sucesso():
    print()
    print('GOOOOOOL!')

# Ordenacao
def ordenar_dicionarios(lista, atributo, eh_decrescente):
    def pegar(item): # função que diz POR QUAL campo ordenar
        return item[atributo]
    return sorted(lista, key=pegar, reverse=eh_decrescente)

def eh_decrescente(comando):
    if comando == 1:
        decrescente = False
    else:
        decrescente = True
    return decrescente

# Filter
def filtrar_atributo(lista, termo, atributo):
    termo = termo.lower()
    encontrados = []
    for item in lista:
        if termo == item[atributo].lower():
                encontrados.append(item)
    return encontrados

def filtrar_atributo_int(lista, atributo):
    encontrados = []
    for item in lista:
        if item[atributo]:
                encontrados.append(item)
    return encontrados

def buscar_nome(lista, termo):
    termo = termo.lower()
    encontrados = []
    for item in lista:
        if termo in item["nome"].lower():
                encontrados.append(item)
    return encontrados

# Reduce
def status_copa(selecoes, jogadores, partidas):
    qtd_selecoes = 0
    qtd_jogadores = 0
    qtd_partidas = 0

    for i in selecoes:
        qtd_selecoes+=1
    for j in jogadores:
        qtd_jogadores+=1
    for k in partidas:
        qtd_partidas+=1
    return qtd_selecoes, qtd_jogadores, qtd_partidas

def gerar_id(lista, primeiro_id):
    if len(lista) == 0:
        return primeiro_id
    maior_id = lista[0]["id"]
    for item in lista:
        if item["id"] > maior_id:
            maior_id = item["id"]
    return maior_id + 1


def existencia_id(lista, atributo):
    for item in lista:
        if atributo == item['id']:
            return True
    return False
       
def listar_por_id(lista):
    for item in lista:
        id = item['id']
        nome = item['nome']
        print(id,' - ', nome)

def exibir_nome_por_id(lista, id_correspondente):
    for item in lista:
        if item['id'] == id_correspondente:
            return item['nome']
    return None
        