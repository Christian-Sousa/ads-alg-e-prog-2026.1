separador = ";"
def montar_linha_selecao(s):
    # transforma o registro (dict) em uma string com os atributos separados por ;
    valores = [
        str(s["id"]),
        s["nome"],
        s["confederacao"],
        s["grupo"],
        str(s["ranking_fifa"]),
        str(s["titulos"]),
    ]
    return separador.join(valores) # junta tudo com ";"

def salvar_selecoes(caminho, selecoes):
    arquivo = open(caminho, "w", encoding="utf-8")
    for s in selecoes:
        linha = montar_linha_selecao(s)
        arquivo.write(linha + "\n") # uma linha por registro
    arquivo.close()
    print("Seleções salvas com sucesso!")

def montar_selecao_da_linha(linha):
    partes = linha.split(separador) # separa a linha de volta em uma lista
    selecao = {
        "id": int(partes[0]), # converte para int o que é número!
        "nome": partes[1],
        "confederacao": partes[2],
        "grupo": partes[3],
        "ranking_fifa": int(partes[4]),
        "titulos": int(partes[5]),
    }
    return selecao

def carregar_selecoes(caminho):
    selecoes = []
    try:
        arquivo = open(caminho, "r", encoding="utf-8")
        for linha in arquivo:
            linha = linha.strip() # remove o "\n" e espaços
            if linha == "": # pula linhas em branco
                continue
            selecoes.append(montar_selecao_da_linha(linha))
        arquivo.close()
    except FileNotFoundError:
        print("Arquivo de seleções ainda não existe. Começando com lista vazia.")
    return selecoes

def linha_valida(linha, qtd_campos):
    partes = linha.split(separador)
    return len(partes) == qtd_campos

def montar_linha_jogador(j):
    # transforma o registro (dict) em uma string com os atributos separados por ;
    valores = [
        str(j["id"]),
        j["nome"],
        str(j["selecao_id"]),
        j["posicao"],
        str(j["idade"]),
        str(j["gols"]),
    ]
    return separador.join(valores) # junta tudo com ";"

def salvar_jogadores(caminho, jogadores):
    arquivo = open(caminho, "w", encoding="utf-8")
    for j in jogadores:
        linha = montar_linha_jogador(j)
        arquivo.write(linha + "\n") # uma linha por registro
    arquivo.close()
    print("Jogadores salvos com sucesso!")

def montar_jogador_da_linha(linha):
    partes = linha.split(separador) # separa a linha de volta em uma lista
    jogador = {
        "id": int(partes[0]), # converte para int o que é número!
        "nome": partes[1],
        "selecao_id": int(partes[2]),
        "posicao": partes[3],
        "idade": int(partes[4]),
        "gols": int(partes[5]),
    }
    return jogador

def carregar_jogadores(caminho):
    jogadores = []
    try:
        arquivo = open(caminho, "r", encoding="utf-8")
        for linha in arquivo:
            linha = linha.strip() # remove o "\n" e espaços
            if linha == "": # pula linhas em branco
                continue
            jogadores.append(montar_jogador_da_linha(linha))
        arquivo.close()
    except FileNotFoundError:
        print("Arquivo de jogadores ainda não existe. Começando com lista vazia.")
    return jogadores