# Copa Manager 2026

Sistema desenvolvido em Python para gerenciamento de seleções,
jogadores e partidas da Copa do Mundo FIFA 2026.

## Funcionalidades

### Seleções
- Cadastrar seleção
- Listar / ordenar seleções
- Buscar seleção pelo nome
- Buscar seleção com filtros
- Exibir número de gols de seleção cadastrada

### Jogadores
- Cadastrar jogador
- Listar jogadores com ordenação
- Filtrar jogadores por atributos
- Exibir artilheiro da copa
- Buscar jogadores por seleção
- Calcular média de idade de jogadores de um seleção

### Partidas
- Cadastrar partida
- Listar partidas

### Estatísticas
- Quantidade de seleções
- Quantidade de jogadores
- Quantidade de partidas

## Estrutura dos dados

### Seleção
    ```python
    {
    'id': 1,
    'nome': 'Brasil',
    'confederacao': 'CONMEBOL',
    'grupo': 'A',
    'ranking_fifa': 5,
    'titulos': 5
    }
    ```
### Jogadores
    ```python
    {
    'id': 101,
    'nome': 'Endrick',
    'selecao_id': 1,
    'posicao': 'Atacante',
    'idade': 19,
    'gols': 0
    }
    ```
### Partidas
    ```python
    {
    'id': 5001,
    'selecao_casa_id': 1,
    'selecao_fora_id': 2,
    'gols_casa': 2,
    'gols_fora': 1,
    'fase': 'Grupo A'
    }
    ```
